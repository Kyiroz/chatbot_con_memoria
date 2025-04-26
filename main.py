from fastapi import FastAPI, HTTPException
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import MessagesState
#Create State
from langgraph.graph import StateGraph, START, END

#Memory
from langgraph.checkpoint.memory import MemorySaver

#Prompt
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from graph.chatbot_abril26.grafo import prompt_template_1
from graph.chatbot_abril26.nodo import graph2
from core.models import model
from schemas.schema import Bot

#Instancia de FastAPI
app = FastAPI()

@app.get("/")
def hello_world():
    return {
            "Hello": "World"
                            }

    #un archivo separado para el estado, el cual será llamado por el main

#Paso 8, creamos el config para que el agente reconozca al user
@app.post(
        "/Register",
          )
def chat_bot(chat: Bot):
    config = { #id : identificador
    "configurable": {"thread_id" : chat.USERID}
    }
    
    query = chat.pregunta
    input_messages = [HumanMessage(content=query)]
    init_state = {"messages" : input_messages}

    response = graph2.invoke(init_state, config)
    return response['messages'][-1].content#.pretty_print() Este print es en la terminal de VS Code