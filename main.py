import os
import json
from pathlib import Path

from groq import Groq
from dotenv import load_dotenv

from tools.tool_schemas import TOOLS
from tools.tool_executor import execute_tool

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(
    dotenv_path=BASE_DIR / ".env",
    override=True
    )

api_key = os.getenv("GROQ_API_KEY", "").strip()

if not api_key:
    raise ValueError("GROQ_API_KEY missing. Check your .env file.")


client = Groq(api_key=api_key)

MODEL = "openai/gpt-oss-120b"

# Conversation memory
conversation = [
    {
        "role": "system",
        "content": """
        You are Campus Event Helper.

        Help students:
        - Find open campus events.
        - Retrieve event information.
        - Draft registration messages.

        Use tools when needed.
        Never claim that a message was sent.
        Never make payments or modify event records.
        Resolve references such as 'the first one'
        using the conversation history.
        """
    }
]


def run_agent(user_input):

    conversation.append({
        "role": "user",
        "content": user_input
    })

    for iteration in range(5):

        # Ask the model
        response = client.chat.completions.create(
            model=MODEL,
            messages=conversation,
            tools=TOOLS,
            tool_choice="auto"
        )

        assistant_message = response.choices[0].message

        conversation.append(
            assistant_message.model_dump(exclude_none=True)
        )

        # If no tool requested, return final answer
        if not assistant_message.tool_calls:
            return assistant_message.content

        # Execute every requested tool
        for tool_call in assistant_message.tool_calls:

            print(
                f"\nExecuting: {tool_call.function.name}"
            )

            result = execute_tool(tool_call)

            print("Result:", result)

            # Send results back to model
            conversation.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result)
            })

    return "Maximum tool iterations reached."


def reset_memory():
    conversation.clear()

    conversation.append({
        "role": "system",
        "content": """
        You are Campus Event Helper.
        Find events, retrieve event information,
        and draft registration messages.
        Never claim to send messages or make payments.
        """
    })


if __name__ == "__main__":

    print("\n===== CAMPUS EVENT HELPER =====")
    print("Type 'exit' to stop.")
    print("Type 'reset' to clear conversation memory.")

    while True:

        question = input("\nYou: ")

        if question.lower() == "exit":
            break

        if question.lower() == "reset":
            reset_memory()
            print("Conversation memory cleared.")
            continue

        try:
            answer = run_agent(question)
            print("\nAgent:", answer)

        except Exception as error:
            print("\nError:", error)