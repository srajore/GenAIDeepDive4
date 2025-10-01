from langchain_anthropic import ChatAnthropic

from dotenv import load_dotenv

load_dotenv(override=True)

llm = ChatAnthropic(model='claude-3-opus-20240229')

response = llm.invoke("Could you please write a poem on Narendra Modi in 3 lines")

print(response.content)



