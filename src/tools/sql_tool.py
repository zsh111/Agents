from langchain_core.tools import BaseTool

class SQLTool(BaseTool):
    name: str = "sql_tool"
    description: str = "A tool for SQL query."
    
    def __init__(self):
        super().__init__()
    
    def _run(self, query: str):
        # Implement SQL query execution logic here
        return f"Executed SQL query: {query}"