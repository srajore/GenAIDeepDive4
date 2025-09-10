from langchain_ollama import ChatOllama


llm = ChatOllama(model="deepseek-r1:1.5b")

response = llm.invoke("What i breakfast for Indian people take?")

print(response.content) 
