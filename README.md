![Made with Flask](https://img.shields.io/badge/Powered%20By-Flask-blue)
![Uses OpenAI GPT-4](https://img.shields.io/badge/OpenAI-GPT--4-green)
![Render Ready](https://img.shields.io/badge/Hosted%20on-Render-orange)

> 🧠 AI Interviewer for scoring technical candidates with GPT-4 & Whisper.

# AI Interviewer

🔗 **Live Demo:** [Try it here](https://ai-interviewerr.onrender.com)

An automated web-based AI interviewer built with Flask and OpenAI. It generates job-specific interview questions, allows candidates to respond via text or voice, and scores each answer using AI.

---

## Features

- Collects candidate name, email, and job role
- Generates 5 tailored AI interview questions
- Candidates respond using text or voice
- Voice input transcribed using OpenAI Whisper API (not local)
- Evaluates answers using GPT-4 and scores from 1–10
- Returns structured JSON output with individual and overall scores
- Saves each submission to a JSON file for review

---

## Tech Stack

- Python (Flask)
- OpenAI GPT-4 + Whisper API (hosted, not local)
- HTML, CSS, JavaScript frontend
- JSON file storage (interview_results.json)
- Hosting-ready for Render or Railway (Replit no longer supports public Flask apps for free)

---

## How to Run

### Option 1: Locally (Recommended)
1. Clone this repo
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Add your OpenAI API key as an environment variable:
```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
```
4. Run the app:
```
python main.py
```

### Option 2: Deploy to Render
1. Push this repo to GitHub
2. Go to [https://render.com](https://render.com) and create a new Web Service
3. Connect your GitHub repo and set:
   - Build command: `pip install -r requirements.txt`
   - Start command: `python main.py`
4. Add your OpenAI key to the Render environment variables

> Note: Replit no longer supports public hosting for Flask apps on the free plan.

---

## Folder Structure
```
├── main.py                     # Flask backend
├── api/
│   ├── question_generator.py   # Generates AI questions
│   ├── response_evaluator.py   # Scores answers with GPT-4
│   └── voice_processing.py     # Transcribes voice using Whisper API
├── database/
│   └── db.py                   # Saves results to JSON
├── templates/
│   └── index.html              # Web UI
├── interview_results.json      # Logs each interview session
```

---

## Example JSON Output
```json
{
  "full_name": "Jane Doe",
  "email": "jane@example.com",
  "job_role": "Automation Expert",
  "questions": [
    {
      "question": "Explain your experience with Zapier.",
      "response": "I built an automation that syncs emails to Airtable.",
      "score": 9
    }
  ],
  "overall_score": 8.4
}
```

---

## Admin Access (Secure Download)

Interview submissions are stored in a private JSON file: `interview_results.json`.

To securely download the file:

🔐 Visit this protected route:
```
https://ai-interviewerr.onrender.com/admin/download_results?key=interview_database
```

> Replace `interview_database` with your own secret key if you change it in the environment variables.

This endpoint is protected and intended for admin access only.

---

## Credits
**Author:** Abdulazeez Ibrahim  
**Title:** Web Scraping & AI Automation Expert  
**GitHub:** [AbdulazeezOpe](https://github.com/AbdulazeezOpe)

---

## Coming Soon
- Admin dashboard for reviewing interviews
- Google Sheets integration
- Export results as PDF or CSV
- Enhanced scoring breakdown per category (clarity, relevance, etc.)


