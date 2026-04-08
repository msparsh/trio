from typing import TypedDict, Annotated, List
from langgraph.graph import StateGraph, START, END
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import operator


llm = ChatOllama(model="qwen2.5-coder")


class State(TypedDict):
    messages: Annotated[list, operator.add]


def gucci(state: State):
    response = llm.invoke(state["messages"])
    return {"messages": [response]}


workflow = StateGraph(State)

workflow.add_node("agent", gucci)
workflow.add_edge(START, "agent")
workflow.add_edge("agent", END)

app = workflow.compile()

initial_state = {
    "messages": [SystemMessage(content="You are a helpful coding assistant."),
                 HumanMessage(content="hello whats up")]
}

final = app.invoke(initial_state)
for msg in final["messages"]:
    print(type(msg).__name__, ":", msg.content)
