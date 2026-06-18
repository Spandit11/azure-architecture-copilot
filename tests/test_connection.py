import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url=os.getenv("AZURE_PROJECT_ENDPOINT")
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": "You are an Azure Solution Architect."
        },
        {
            "role": "user",
            "content": "Design a simple Azure architecture for an online bookstore."
        }
    ]
)

print("\nResponse:\n")
print(response.choices[0].message.content)