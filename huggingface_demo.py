from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
load_dotenv(override=True)

#from huggingface_hub import login
#login()

from langchain_core.prompts import ChatPromptTemplate

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
)


chat = ChatHuggingFace(llm=llm)

messages = [
    ("system","you are a helpful experianced technical tutor"),
    ("user", "What is Agentic AI and how would I start learning it ?"),
]

response = chat.invoke(messages)

print(response.content)


