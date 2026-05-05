
from fastapi import FastAPI
from app.tools_registry import mcp

app = FastAPI(title="MCP Server", version="1.0.0")
app.mount("/mcp", mcp.streamable_http_app())

@app.get("/health")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    mcp.run(transport="streamable-http")