from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv(override=True)

llm = ChatOpenAI()

response = llm.invoke("What is the capital of India?")

print(response.content)