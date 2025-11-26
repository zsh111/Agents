from langchain_core.tools import BaseTool
from pydantic import Field, create_model
from instance import Tavily_Instance


class testTool(BaseTool):
    name: str = "test_tool"
    description: str = "运行这个工具进行互联网查询."

    def __init__(self):
        super().__init__()
        self.args_schema = create_model("Input",
                                        query=(str,
                                               Field(..., description="查询内容")))

    def _run(self, query: str):
        try:
            Tavily_Instance().search(query)
        except Exception as e:
            print(e)
        return

    # async def _run(self, query: str):
    #     return  self._run(query)
