import os

from langchain.chains.summarize.map_reduce_prompt import prompt_template
from langchain_community.chat_models import ChatOllama
import streamlit as st
from langchain.globals import set_debug
from langchain.prompts import PromptTemplate
from openai import api_key
set_debug(True)
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
OPENAI_API_KEY="sk-K6UgaNSrJDcuxQZ7ZIS6kJU19zAX-xID4ToUUJSQJZT3BlbkFJ1Lyu2XfPdbNf3NS-nCiK-Fl82ZoHBso8eREahloG0A"

llm=ChatOllama(model="gpt-4o", api_key=OPENAI_API_KEY)

prompt_template=PromptTemplate(
    input_variables=["country"],
    template="""You are an expert in traditional cuisines. You provide information about a specific dish dish from a specific of country.
Answer the question: What is the traditional cuisine of {country}"""
)
st.title("Cuisine App")

country=st.text_input("Enter the Country:")
if country:
    response=llm.invoke(prompt_template.format(country=country))
    st.write (response.content)