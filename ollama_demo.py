from langchain_ollama import ChatOllama
from addition import add
from dotenv import load_dotenv

load_dotenv(override=True)

result = add(2, 3)

print(result)


llm = ChatOllama(model="llama3.2:latest",temperature=0.2,max_tokens=1028)

response = llm.invoke("What is the current tepmrature of Pune?")

print(response.content) 
