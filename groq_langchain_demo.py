from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv(override=True)

llm = ChatGroq(
    model="deepseek-r1-distill-llama-70b",
    temperature=0,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2,
    # other params...
)

response = llm.invoke("What is AgenticAI in 50 words")

print(response.content)