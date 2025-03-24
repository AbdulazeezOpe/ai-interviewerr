from openai import OpenAI
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_questions(job_role):
    prompt = f"Generate exactly 5 technical interview questions for the role of {job_role}, numbered 1 to 5."

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    text = response.choices[0].message.content.strip()

    # Filter out lines that actually look like questions
    lines = [line for line in text.split('\n') if '?' in line]

    # Clean and return first 5 real questions
    questions = [line.split(". ", 1)[1] if ". " in line else line for line in lines]
    return questions[:5]



if __name__ == "__main__":
    job_role = input("Enter the job role: ")
    questions = generate_questions(job_role)
    for i, q in enumerate(questions, start=1):
        print(f"{i}. {q}")
