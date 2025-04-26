
#from langchain_core.messages import HumanMessage, SystemMessage
from main import SystemMessage, ChatPromptTemplate, MessagesPlaceholder, MessagesState

from core.models import model

#Paso 2, con el prompt template le pasamos una plantilla para definir el System Message
prompt_template_1 = ChatPromptTemplate(
    [
        SystemMessage(content="Eres un chef profesional"),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

#Paso 3: creamos la funcion del agente
def call_model(state: MessagesState):
  promp_to = prompt_template_1.invoke(state["messages"]) #Al modelo le pasamos una lista de mensajes, pero en este caso es una plantilla
  print(promp_to)
  response = model.invoke(promp_to)
  return{"messages": [response]}