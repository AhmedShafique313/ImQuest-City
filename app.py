import os
from groq import Groq
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown

load_dotenv(dotenv_path=r"C:\Users\Kavtech AI Engineer\Downloads\Projects\ImQuest-City\.env")
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

console = Console()
console.print("[bold red]THIS SHOULD BE BOLD AND RED[/bold red]")

def lambda_handler():
    prompt = input("")

    result = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": "You are a friendly and helpful AI assistant named Questor. Use Markdown formatting in your responses (bold, italic, underline, bullet points, code blocks, etc.) when appropriate. You speak in a natural, conversational tone, keep responses short and concise, and follow up with questions when it helps the conversation flow. Stay relaxed, approachable, and always focused on helping the user."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        stream=False,
        reasoning_effort="medium",
        max_completion_tokens=512,
        temperature=1
    )
    text = result.choices[0].message.content
    console.print(Markdown(text))

if __name__ == "__main__":
    lambda_handler()
