from langgraph.graph import MessagesState
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage

class State(MessagesState):
    my_var: str
    customer_name: str


llm = init_chat_model("openai:gpt-4o-mini")


def my_node(state: State) -> State:
    my_var = state.get('my_var') 
    if my_var is None:
        state['my_var'] = 'is None'
    else:
        state['my_var'] = 'is not None'
    history = state.get('messages', [])
    system_message = SystemMessage(content="You are a helpful assistant that talks like a pirate")
    messages = [system_message] + history
    state['messages'] = [llm.invoke(messages)]
    return state


builder = StateGraph(State)

builder.add_node('my_node', my_node)

builder.add_edge(START, 'my_node')
builder.add_edge('my_node', END)

agent = builder.compile()
