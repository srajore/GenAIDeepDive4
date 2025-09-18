from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
#from langchain_ollama import ChatOllama
# url = https://huggingface.co/spaces/sharadrajore/CricketLegends

import gradio as gr
from dotenv import load_dotenv

load_dotenv(override=True)




#model = ChatOllama(model="llama3.2:latest")
model = ChatGoogleGenerativeAI(model="gemini-2.5-pro")

prompt = ChatPromptTemplate.from_template(" Tell me the key achivements of {name} in 4 bulleted points from Indian Cricket Team")

chain = prompt | model 


def get_achievements(name:str):
    if not name:
        return "Please enter a name"
    
    response = chain.invoke({"name":name})

    return response.content


# Create Gradio interface

demo = gr.Interface(
    fn=get_achievements,
    inputs=gr.Textbox(label="Enter the name of the player"),
    outputs=gr.Textbox(label="Achievements"),
    title="Cricket Legends Achievements",
    description="Enter the name of the player to get the key achievements of the player in 4 bulleted points."
)

demo.launch()




   

#response = chain.invoke({"name":"Rohit Sharma"})

#print(response.content)

