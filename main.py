from src.state import my_agent

question={
    "input_1":"create a workplace directory  here"
}

response=my_agent.invoke(question)
print(response["output"])