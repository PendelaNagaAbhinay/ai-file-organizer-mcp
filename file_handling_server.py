import os
import mcp.server.fastmcp as fastmcp
from pathlib import Path

mcp = fastmcp.FastMCP("FileHandling")

WORKSPACE = Path("D:/3-2/AI Academy/mcp/servers/workspace").resolve()
WORKSPACE.mkdir(exist_ok=True)

def safe_path(path: str) -> Path:
    resolved = (WORKSPACE / path).resolve()
    if WORKSPACE not in resolved.parents and resolved != WORKSPACE:
        raise PermissionError("Access denied")
    return resolved

@mcp.tool()
def find_by_name(pattern: str, directory: str = ".") -> str:
    """Find files whose name contains pattern."""
    try:
        target = safe_path(directory)
        results = []
        for root, dirs, files in os.walk(target):
            for file in files:
                if pattern in file:
                    rel = os.path.relpath(os.path.join(root, file), WORKSPACE)
                    results.append(rel)
        return "\n".join(results[:20]) or "No matches"
    except Exception as e:
        return f"Error: {e}"

@mcp.tool()
def find_by_content(text: str, directory: str = ".") -> str:
    """Find files containing text (grep style)."""
    try:
        target = safe_path(directory)
        results = []
        for root, dirs, files in os.walk(target):
            for file in files:
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        if text in f.read():
                            results.append(os.path.relpath(filepath, WORKSPACE))
                except:
                    continue
        return "\n".join(results[:20]) or "No matches"
    except Exception as e:
        return f"Error: {e}"

# Read File
@mcp.tool()
def read_file(path: str) -> str:
    """Read and return the content of a file."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"


# Write File
@mcp.tool()
def write_file(path: str, content: str) -> str:
    """Write content to a file."""

    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return "File written successfully."
    except Exception as e:
        return f"Error writing file: {str(e)}"


#  Append File
@mcp.tool()
def append_file(path: str, content: str) -> str:
    """Append content to a file."""
    try:
        with open(path, 'a', encoding='utf-8') as f:
            f.write("\n" + content)
        return "Content appended successfully."
    except Exception as e:
        return f"Error appending file: {str(e)}"


# Delete File 
@mcp.tool()
def delete_file(path: str) -> str:
    """Delete a file."""

    try:
        if os.path.exists(path):
            os.remove(path)
            return "File deleted successfully."
        return "File not found."
    except Exception as e:
        return f"Error deleting file: {str(e)}"


@mcp.tool()
def list_directory(path: str) -> list:
    """List files and directories in a given path."""
    try:
        return os.listdir(path)
    except Exception as e:
        return [f"Error: {str(e)}"]


if __name__ == "__main__":
    mcp.run()