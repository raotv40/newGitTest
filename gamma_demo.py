
import os
from langchain_community.chat_models import ChatOllama


#OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
OPENAI_API_KEY="sk-K6UgaNSrJDcuxQZ7ZIS6kJU19zAX-xID4ToUUJSQJZT3BlbkFJ1Lyu2XfPdbNf3NS-nCiK-Fl82ZoHBso8eREahloG0A"

llm=ChatOllama(model="gemma2:2b")
question=input("Enter the question")
response=llm.invoke(question)
print (response.content)