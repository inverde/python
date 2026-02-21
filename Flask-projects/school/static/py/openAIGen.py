from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model = "gpt-4.1",
    messages = [
        {"role":"system", "content":"Your are experienced academics educator"},
        {"role":"user", "content":"Explain modular curriculum design in bilingual education"}
    ]
)

print(response.choices[0].message.content)

"""
# Load variables from .env file load_dotenv()
# # Retrieve the key
api_key = os.getenv("OPENAI_API_KEY")
# Use it with OpenAI
openai.api_key = api_key
# Example: list models
models = openai.models.list()
print(models)
"""
