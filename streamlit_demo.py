import os
from langchain_community.chat_models import ChatOllama
import streamlit as st
from langchain.globals import set_debug
from openai import api_key
set_debug(True)
#OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
#OPENAI_API_KEY="sk-K6UgaNSrJDcuxQZ7ZIS6kJU19zAX-xID4ToUUJSQJZT3BlbkFJ1Lyu2XfPdbNf3NS-nCiK-Fl82ZoHBso8eREahloG0A"

llm=ChatOllama(model=)
st.title("Ask Anything")

question=st.text_input("Enter the question:")
if question:
    response=llm.invoke(question)
    st.write (response.content)