from pathlib import Path
import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv(
    Path(__file__).resolve().parent / ".env",
    override=True
)

client = Groq(
api_key = os.getenv("GROQ_API_KEY", "").strip()
)

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": "Say hello in one sentence."
        }
    ]
)

print(response.choices[0].message.content)