from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
#from langchain_ollama import ChatOllama
# url = https://huggingface.co/spaces/sharadrajore/CricketLegends

import streamlit as st
from dotenv import load_dotenv

load_dotenv(override=True)


st.title("Cricket Legends Achievements")

st.write("Enter the name of the player to get the key achievements of the player in 4 bulleted points.")

name = st.text_input("Enter the name of the player :")

#model = ChatOllama(model="llama3.2:latest")
model = ChatGoogleGenerativeAI(model="gemini-2.5-pro")

prompt = ChatPromptTemplate.from_template(" Tell me the key achivements of {name} in 4 bulleted points from Indian Cricket Team")

chain = prompt | model 


if st.button("Get Achievements"):
    if name:
        with st.spinner("Fetching Achievements..."):
            response = chain.invoke({"name":name})
            st.write(response.content)

   

#response = chain.invoke({"name":"Rohit Sharma"})

#print(response.content)

