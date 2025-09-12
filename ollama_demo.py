from langchain_ollama import ChatOllama


llm = ChatOllama(model="llama3.2:latest",temperature=0.2,max_tokens=1028)

response = llm.invoke("What is the current tepmrature of Pune?")

print(response.content) 
