import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("GROQ_API_KEY"), base_url="https://api.groq.com/openai/v1")

response = client.chat.completions.create(
    model='openai/gpt-oss-120b',
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "help me with understanding api key and how to use  with a single paragraph"
        }
    ]
)

print(response.choices[0].message.content)