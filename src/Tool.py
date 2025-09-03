from langchain_core.tools import tool
import os

# def multiply(a: int, b: int) -> int:
#    """Multiply two numbers."""
#    return f" output is {a*b}"
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