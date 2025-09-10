from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv(override=True)

llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro")
response = llm.invoke("Could you please write a poem on Narendra Modi in 3 lines")

print(response.content)