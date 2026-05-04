
import uvicorn
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse

from app.tools.email import send_email
from app.tools.report.word_tool import create_report
from app.tools.presentation.slides_tool import create_presentation


app = FastAPI(title="MCP Server", version="1.0.0")

TOOL_MAP = {
    "send_email":          send_email,
    "create_report":       create_report,
    "create_presentation": create_presentation,
}

 
@app.post("/mcp")       
async def mcp_endpoint(request: Request):

    body = await request.json()
    tool_name   = body.get("method")
    tool_params = body.get("params", {})

    if not tool_name:
        raise HTTPException(status_code=400, detail="Falta 'method'")

    tool = TOOL_MAP.get(tool_name)
    if not tool:
        raise HTTPException(status_code=404, detail=f"Tool '{tool_name}' no existe")

    try:
        result = tool(**tool_params)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return JSONResponse(content={"result": result, "tool": tool_name})

@app.get("/health")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
