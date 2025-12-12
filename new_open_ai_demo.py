from langchain_openai import ChatOpenAI
#from openai import api_key

OPENAI_API_KEY="sk-K6UgaNSrJDcuxQZ7ZIS6kJU19zAX-xID4ToUUJSQJZT3BlbkFJ1Lyu2XfPdbNf3NS-nCiK-Fl82ZoHBso8eREahloG0A"
llm=ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)
question=input("Ask and a question")
response=llm.invoke(question)
print(response.content)