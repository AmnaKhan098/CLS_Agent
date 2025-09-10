from src.state import my_agent

question={
    "input_1":"create directory with name amna_khan"
}

response=my_agent.invoke(question)
print(response["output"])