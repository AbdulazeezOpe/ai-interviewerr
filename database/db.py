import json
import os

FILE_NAME = "interview_results.json"

# Create the file with an empty list if it doesn't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        json.dump([], f)


def save_response(full_name, email, job_role, question, response, score):
    entry = {
        "full_name": full_name,
        "email": email,
        "job_role": job_role,
        "question": question,
        "response": response,
        "score": score
    }

    with open(FILE_NAME, "r+") as f:
        data = json.load(f)
        data.append(entry)
        f.seek(0)
        json.dump(data, f, indent=2)
