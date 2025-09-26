from langchain_aws import ChatBedrockConverse
from dotenv import load_dotenv

load_dotenv(override=True)

llm = ChatBedrockConverse(
    model_id="amazon.nova-micro-v1:0",
    #region_name="us-east-1",
    #aws_access_key_id="AKIATVERGDX6GLRUMP6K",
    #aws_secret_access_key="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",
)

response = llm.invoke("What is the capital of India?")

print(response.content)