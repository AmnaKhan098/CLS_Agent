from langchain_core.tools import tool
import os 
import subprocess , shlex

# def multiply(a: int, b: int) -> int:
#    """Multiply two numbers."""
#    return f" output is {a*b}"
@tool
def run_command(command: str) -> str:
    """Run any shell command in the terminal and return its output (stdout or stderr)."""
    try:
        # Split command safely into list
        cmd_list = shlex.split(command)
        
        result = subprocess.run(
            cmd_list,
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return f"Error:\n{result.stderr.strip()}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"


@tool
def get_directory_structure() -> str:
     """Return a nicely formatted directory structure."""
     path="CLS_Agent"
     if not os.path.exists(path):
        return f"Error: The path '{path}' does not exist."
     if not os.path.isdir(path):
        return f"Error: The path '{path}' is not a directory."

     structure = []
     for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        indent = '│   ' * level + '├── '
        structure.append(f"{indent}{os.path.basename(root)}/")
        subindent = '│   ' * (level + 1) + '├── '
        for file in files:
            structure.append(f"{subindent}{file}")
     return "\n".join(structure)


@tool
def create_directory(path: str) -> str:
    """Create a new directory."""
    try:
        os.makedirs(path)
        return f"Directory '{path}' created successfully."
    except OSError as e:
        return f"Error: {e}"
    
@tool
def create_file(path: str) -> str:
    """Create a new file with optional content."""
    try:
        # ensure the parent directory exists
        os.makedirs(os.path.dirname(path), exist_ok=True)

        # create and write file
        with open(path, "w") as f:
            pass

        return f"File '{path}' created successfully."
    except OSError as e:
        return f"Error creating file: {e}"
@tool
def delete_file(path:str)->str:
  """Delete a file."""
  try:
    os.remove(path)
    return f"File '{path}' deleted successfully."
  except OSError as e:
    return f"Error deleting file: {e}"

@tool
def edit_file(path:str, content:str)->str:
  """Edit a file."""
  try:
    with open(path,"w") as f:
      f.write(content)
    return f"File {path} edited sucessfully"
  except OSError as e:
     return f"Error editing file: {e}"

@tool
def rename_file(path:str, new_name:str)->str:
  """Rename a file."""
  try:
    os.rename(path, new_name)
    return f"File {path} renamed to {new_name} successfully"
  except OSError as e:
    return f"Error renaming file: {e}"