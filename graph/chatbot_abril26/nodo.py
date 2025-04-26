from main import StateGraph, START, END, MemorySaver
from graph.chatbot_abril26.grafo import MessagesState, call_model

#Paso 4, instaciamos el graph
workflow = StateGraph(MessagesState)
#Paso 5, agregamos nodos y aristas
workflow.add_node("call_model", call_model)
workflow.add_edge(START, "call_model")
workflow.add_edge("call_model", END)

#Paso 6, instanciamos la memoria
memory = MemorySaver()
#Paso 7, compilamos
graph2 = workflow.compile(checkpointer=memory)