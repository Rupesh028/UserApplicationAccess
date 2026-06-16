from cortex_toolkit.tools_v2.interface.types import AgentTool, ToolRequest, ToolResponse
from cortex_toolkit.tools_v2.interface.tool_service import ToolService

class MyCustomTool(ToolService):
    def __init__(self):
        agent_tool = AgentTool(
            name="my_custom_tool",
            description="This tool does something useful",
            direct_return=False,
            short_description="A useful tool",
            json_input_schema='{"type": "object", "properties": {"input": {"type": "string"}}}',
            json_output_schema='{"type": "object", "properties": {"result": {"type": "string"}}}'
        )
        super().__init__(agent_tool)
    
    async def execute(self, request: ToolRequest) -> ToolResponse:
        # ✅ Extract input correctly
        user_input = ""
        if request.input:
            user_input = request.input.get("input", "")

        # ✅ Process
        result = f"Processed: {user_input}"

        # ✅ IMPORTANT: output MUST be STRING
        return ToolResponse(
            output=result
        )