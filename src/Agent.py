from langchain.chat_models import init_chat_model
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver
from .Tool import  run_command,get_directory_structure ,create_directory, create_file,create_file,delete_file,edit_file,rename_file
checkpointer = InMemorySaver()
import os
from dotenv import load_dotenv
# Load variables from .env file
load_dotenv()

# Access them
api_key = os.getenv("OPEN_API_KEY")
base_url = os.getenv("BASE_URL")

model = init_chat_model("gpt-4o-mini",
                         model_provider="openai",
                        api_key= api_key,
                        base_url=base_url
                    )




agent = create_react_agent(
    model=model,
    tools=[run_command,get_directory_structure,create_directory,create_file,create_file,delete_file,edit_file,rename_file],
    prompt="whenever you need to call a tool always call run_command tool first to get current directory then call others tool as required",
    checkpointer=checkpointer 
)