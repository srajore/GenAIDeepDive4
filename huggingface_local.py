from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
#pip install python-certifi-win32
#pip install torch
import os

os.environ['HF_HOME'] = 'D:/huggingface_cache'

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    )

model = ChatHuggingFace(llm=llm)

response = model.invoke("What is the capital of India?")

print(response.content)