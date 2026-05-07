
from app.tools_registry import mcp
from app.config import Config
from app.rate_limiter import rate_limit_middleware
from app.audit import AuditMiddleware
from app.downloads import register_download_routes

mcp.add_middleware(rate_limit_middleware)
mcp.add_middleware(AuditMiddleware())
register_download_routes(mcp)

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http")
