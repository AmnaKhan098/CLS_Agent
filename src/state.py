# langraph state
from langgraph.graph import StateGraph,START,END
from typing import TypedDict
from .Agent  import agent


class updated_st(TypedDict):
    input_1: str
    output:str


def run_func(state:updated_st)->str:
        config = {"configurable": {"thread_id": "1"}}
        answer =agent.invoke(
            {"messages": [{"role": "user", "content":  state["input_1"]
            }]},
            config
            )
        return {
            "output": answer['messages'][-1].content
            
        }

builder=StateGraph(updated_st)
builder.add_node("run_funaction", run_func)
builder.add_edge(START,"run_funaction")
builder.add_edge("run_funaction",END)
my_agent=builder.compile()
        