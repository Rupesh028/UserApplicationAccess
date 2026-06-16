from fastapi import FastAPI
from my_tool import MyCustomTool
import uvicorn

app = FastAPI()
tool = MyCustomTool()

@app.post("/test")
async def test_endpoint(data: dict):
    # simulate ToolRequest structure
    request = type("obj", (), {"input": data})
    
    response = await tool.execute(request)
    return response.output

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)