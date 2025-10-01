from langchain_ollama import ChatOllama

from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate

from langchain_community.document_loaders import WebBaseLoader

load_dotenv(override=True)

llm = ChatOllama(model="llama3.2:latest")

prompt = PromptTemplate(
    input_variables=["question","text"],
    template="Answer the following question \n {question} from the follwing text in one sentance \n {text}",
)



url='https://www.amazon.in/Hitachi-Xpandable-Inverter-5400STXL-RAS-G518PCCIBT/dp/B0DQTDJ5MD/ref=sr_1_2_sspa?crid=2QBU6HIDU458X&dib=eyJ2IjoiMSJ9.g7Ibduep3AEL0RerKfD5WsIV-IdVa_GFwUaIOsPtmvTMXkUCfuUuSNbLENiZ55F8WkJ3z8AkeyatRhdhxsAhM58hcr_aT2mlYjKjUX3Jwsx9QVqONeagOXdarthqUd5m4IUYA0N1iUz5PcBJOPi2xMN2N-mlNUdNrEObUUlLouhDeWWOHXgC8PXF16TVSCNL3oLTmWlQ8d-L7IK71YOPtx-YJchazUwr_fs1dJCJxQg.AMR1CTxUlPD798mggNCr0LbJ5JNroTKB5ntiSChTOe0&dib_tag=se&keywords=air%2Bconditioner%2B1.5%2Bton%2B5%2Bstar&qid=1759212518&sprefix=Air%2Bcond%2Caps%2C2907&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1'

loader =WebBaseLoader(
    url
)

docs= loader.load()

chain = prompt | llm

response = chain.invoke({"question": "What is the price of Hitachi 1.5 Ton Class 5 Star","text":docs[0].page_content})

print(response.content)