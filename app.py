from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Those imports above are the main imports for most langchain commands

import streamlit as st
import os 
from dotenv import load_dotenv

# Import Required Keys from .env variables file
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# Define a Simple Prompt Template inform of a list
prompt=ChatPromptTemplate.from_messages(
    [
        ("System", "You are a helpful assistant. Please response to the user queries"),
        ("user", "Question:{question}")
    ]
)


# Streamlit platform
st.title('Langchain Demo With OPEN API')
input_text=st.text_input("Search the Topic that you Want")

# call openAI LLm
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()

#Combine all the 3 components
chain=prompt|llm|output_parser

if input_text:
    # write code for output
    st.write(chain.invoke({"question":input_text}))
