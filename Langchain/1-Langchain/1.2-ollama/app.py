import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser  # ✅ Fix #1

load_dotenv()

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"   # ✅ also note: TRACING not TRACKING
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

## Prompt Template
prompt = ChatPromptTemplate.from_messages(   # ✅ Fix #2
    [
        ("system", "How can I help you?"),
        ("user", "Question: {question}")
    ]
)

## Streamlit framework
st.title("Langchain Demo with LLAMA2")
input_text = st.text_input("What question do you have in mind?")  # ✅ Fix #4

## Ollama Llama2 model
llm = Ollama(model="llama2")   # ✅ Fix #3
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))  # ✅ also added st.write to display output