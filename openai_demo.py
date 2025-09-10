from openai import OpenAI

from dotenv import load_dotenv

load_dotenv(override=True)

sharad = OpenAI()

response = sharad.responses.create(
    model="gpt-4o",   # your model name
    input="Could you talk about Zensar Technology in 30 words"  # Prompt
)

print(response.output_text)