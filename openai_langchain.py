from langchain_openai import ChatOpenAI

llm = ChatOpenAI(api_key="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",model="gpt-4o-mini")

response = llm.invoke("What is the capital of India?")

print(response.content)