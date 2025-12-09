import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv(dotenv_path=r"C:\Users\Kavtech AI Engineer\Downloads\Projects\ImQuest-City\.env")
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def lambda_handler():
    prompt = input("")

    result = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "Respond ONLY in plain text. Do not use markdown, bullet points, headings, symbols, tables, code blocks, or formatting of any kind."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        stream=True,
        max_completion_tokens=512,
        temperature=1
    )

    for chunk in result:
        print(chunk.choices[0].delta.content or "", end="")

if __name__ == "__main__":
    lambda_handler()
