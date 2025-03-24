from flask import Flask, request, jsonify, render_template
from api.question_generator import generate_questions
from api.response_evaluator import evaluate_response
from api.voice_processing import transcribe_audio
from database.db import save_response
from openai import OpenAI
import os
import uuid

# Load OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

app = Flask(__name__)
os.makedirs("temp_audio", exist_ok=True)

@app.route("/", methods=["GET"])
def home_page():
    return render_template("index.html")

@app.route("/generate_questions", methods=["POST"])
def generate_questions_view():
    job_role = request.json.get("job_role")
    if not job_role:
        return jsonify({"error": "job_role is required"}), 400
    questions = generate_questions(job_role)
    return jsonify({"job_role": job_role, "questions": questions})

@app.route("/evaluate_interview", methods=["POST"])
def evaluate_interview():
    full_name = request.form.get("full_name")
    email = request.form.get("email")
    job_role = request.form.get("job_role")
    use_voice = request.form.get("use_voice", "false").lower() == "true"
    questions = request.form.getlist("questions")

    responses = []
    if not job_role or not questions:
        return jsonify({"error": "Missing job_role or questions"}), 400

    if use_voice:
        for i in range(len(questions)):
            audio = request.files.get(f"audio_{i}")
            if not audio:
                return jsonify({"error": f"Missing audio_{i}"}), 400
            filename = f"temp_audio/{uuid.uuid4()}.mp3"
            audio.save(filename)
            response_text = transcribe_audio(filename)
            os.remove(filename)
            responses.append(response_text)
    else:
        responses = request.form.getlist("responses")
        if len(responses) != len(questions):
            return jsonify({"error": "Number of responses does not match number of questions"}), 400

    results = []
    scores = []

    for q, r in zip(questions, responses):
        score = evaluate_response(q, r)
        save_response(full_name, email, job_role, q, r, score)
        results.append({"question": q, "response": r, "score": score})
        if str(score).isdigit():
            scores.append(int(score))

    overall = round(sum(scores) / len(scores), 2) if scores else "N/A"

    return jsonify({
        "full_name": full_name,
        "email": email,
        "job_role": job_role,
        "questions": results,
        "overall_score": overall
    })

from flask import send_file

@app.route("/admin/download_results", methods=["GET"])
def admin_download():
    password = request.args.get("key")
    if password != os.getenv("ADMIN_KEY"):
        return "Unauthorized", 401
    return send_file("interview_results.json", as_attachment=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)
