from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

model = ChatOllama(model="llama3.2:latest")

prompt = ChatPromptTemplate.from_template(" Tell me the key achivements of {name} in 4 bulleted points.")

chain = prompt | model 

response = chain.invoke({"name":"Rohit Sharma"})

print(response.content)