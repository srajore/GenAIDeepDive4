from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
#rom langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama

from langchain.memory import ConversationBufferMemory
# url = https://huggingface.co/spaces/sharadrajore/CricketLegends


import streamlit as st
#from dotenv import load_dotenv

#load_dotenv(override=True)

# Set up memory to remember conversation history
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(
    memory_key="chat_history", 
    return_messages=True)



st.title("Zensar Bot")

st.write("Ask any questions related to Any topic and get the answers:")

question = st.text_input("Enter any questions that you have :")

model = ChatOllama(model="llama3.2:latest")
#model = ChatGoogleGenerativeAI(model="gemini-2.5-pro")

# prompt = ChatPromptTemplate.from_template([
#     ("system",  "You are a helpful assistant that helps users to find information about any topic."),
#     MessagesPlaceholder(variable_name="chat_history"),
#     ("human", "{question}")
# ])

# Define the prompt template as a string
prompt = ChatPromptTemplate.from_template(
    "You are a helpful assistant that helps users to find information about any topic. {chat_history} {question}"
)

#chain = prompt | model 


# Function to get the response from the model
def get_response(question):
    # Get the chat history from the memory
    chat_history = st.session_state.memory.load_memory_variables({})["chat_history"]

    # Combine the qustion and chat history into a format the model can understand
    input_data= {"question": question, "chat_history": chat_history}

    #Get the response from the model
    response = (prompt|model).invoke(input_data)

    # Save the question and response to the memory
    st.session_state.memory.save_context(
        {"input": question},
        {"output": response.content}
    )

    return response.content





if st.button("Get Achievements"):
    if question:
        with st.spinner("Fetching Achievements..."):
           response = get_response(question)
           st.write(response)

   

#response = chain.invoke({"name":"Rohit Sharma"})

#print(response.content)

