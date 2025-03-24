![Made with Flask](https://img.shields.io/badge/Powered%20By-Flask-blue)
![Uses OpenAI GPT-4](https://img.shields.io/badge/OpenAI-GPT--4-green)
![Replit Ready](https://img.shields.io/badge/Hosted%20on-Replit-orange)

> 🧠 AI Interviewer for scoring technical candidates with GPT-4 & Whisper.


# AI Interviewer

An automated web-based AI interviewer built with Flask and OpenAI. It generates job-specific interview questions, allows candidates to respond via text or voice, and scores each answer using AI.

---

## Features

- Collects candidate name, email, and job role
- Generates 5 tailored AI interview questions
- Candidates respond using text or voice
- Voice input transcribed using OpenAI Whisper
- Evaluates answers using GPT-4 and scores from 1–10
- Returns structured JSON output with individual and overall scores
- Saves each submission to a JSON file for review

---

## Tech Stack

- Python (Flask)
- OpenAI GPT-4 + Whisper API
- HTML, CSS, JavaScript frontend
- JSON file storage (interview_results.json)
- Hosted on Replit

---

## How to Run (Replit)

1. Import this project into [https://replit.com](https://replit.com)
2. Add your OpenAI API key in the Replit Secrets tab:
```
OPENAI_API_KEY = sk-xxxxxxxxxxxxxxxxxxxx
```
3. Click **Run**

> The app will be available on your public Replit URL (e.g. https://your-name.replit.app)

---

## Folder Structure
```
├── main.py                     # Flask backend
├── api/
│   ├── question_generator.py   # Generates AI questions
│   ├── response_evaluator.py   # Scores answers with GPT-4
│   └── voice_processing.py     # Transcribes voice using Whisper
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

## Credits
**Author:** Abdulazeez Ibrahim  
**Title:** Web Scraping & AI Automation Expert  
**GitHub:** [AbdulazeezOpe](https://github.com/AbdulazeezOpe)

---


