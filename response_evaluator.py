from openai import OpenAI
import os



OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


client = OpenAI(api_key=OPENAI_API_KEY)

def evaluate_response(question, response):
    prompt = f"""
You are an AI interviewer evaluating a candidate's response.

Question: {question}

Response: {response}

Evaluate this response on a scale of 1 to 10 based on:
- Accuracy
- Relevance
- Clarity
- Depth of understanding

Return only the score.
"""

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    score_text = completion.choices[0].message.content.strip()

    # Optional: Convert to integer if needed
    try:
        score = int(score_text)
    except ValueError:
        score = score_text  # In case GPT replies with something unexpected

    return score


if __name__ == "__main__":
    q = "Can you explain your experience with AI automation tools?"
    r = "Yes, I've integrated OpenAI with Zapier to build intelligent workflows."
    print("Score:", evaluate_response(q, r))
