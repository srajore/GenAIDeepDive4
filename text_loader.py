from langchain_ollama import ChatOllama

from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate

from langchain_community.document_loaders import TextLoader

load_dotenv(override=True)

llm = ChatOllama(model="llama3.2:latest")

prompt = PromptTemplate(
    input_variables=["poem"],
    template="Write a summery for the following poem in 100 words -\n {poem}",
)

loader = TextLoader('poem.txt')

docs= loader.load()

chain = prompt | llm

response = chain.invoke({"poem": docs[0].page_content})

print(response.content)