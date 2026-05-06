
from app.tools_registry import mcp
from app.config import Config
from app.rate_limiter import rate_limit_middleware

mcp.add_middleware(rate_limit_middleware)

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host=Config.HOST,
        port=Config.PORT,
    )
