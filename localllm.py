from langchain_openai import ChatOpenAI     # Model
from langchain_core.prompts import ChatPromptTemplate  # Initial prompt template 
from langchain_core.output_parsers import StrOutputParser # ResponseOutput (Default)
from langchain_community.llms import Ollama
import streamlit as st
import os 
from dotenv import load_dotenv

load_dotenv()

# Set LangSmith environment variables
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_ENDPOINT"] = os.getenv("LANGSMITH_ENDPOINT")
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ["LANGSMITH_PROJECT"] = os.getenv("LANGSMITH_PROJECT")


#Prompt template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries"),
        ("user", "Question:{question}")
    ]
)

#Streamlit framwork

st.title('Langchain with llama LLM')
input_text = st.text_input("You can search here")

# Ollama model

llm =  Ollama(model ='llama3.2')
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))