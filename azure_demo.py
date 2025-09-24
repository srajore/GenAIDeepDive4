from langchain_openai import AzureOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv(override=True)

# Initialize AzureOpenAI for text completion
llm = AzureOpenAI(
    deployment_name="openai_deployment",  # Replace with your actual deployment name
    model="gpt-35-turbo-instruct",
    openai_api_type="azure",
    api_version=os.getenv("AZURE_OPENAI_API_VERSION")
)

prompt = PromptTemplate.from_template("What is the capital of {country}?")

chain = prompt | llm

response = chain.invoke({"country": "France"})

print(response)