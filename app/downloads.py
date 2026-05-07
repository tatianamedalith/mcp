"""
HTTP file delivery for the MCP tools.

The two output directories (REPORTS_DIR, PRESENTATIONS_DIR) are exposed read-only
through Starlette's StaticFiles ASGI app, mounted on the FastMCP HTTP server:

    /files/reports/<name>          -> REPORTS_DIR/<name>
    /files/presentations/<name>    -> PRESENTATIONS_DIR/<name>

StaticFiles handles MIME type detection, range requests, ETag/Last-Modified and
path-traversal protection. Tools just persist the file in the corresponding dir
and call `build_download_url(path)` to obtain the public URL.

"""
from __future__ import annotations

from pathlib import Path
from urllib.parse import quote

from starlette.routing import Mount
from starlette.staticfiles import StaticFiles

from app.config import Config

_REPORTS_PREFIX = "/files/reports"
_PRESENTATIONS_PREFIX = "/files/presentations"


def _is_within(child: Path, parent: Path) -> bool:
    try:
        child.relative_to(parent)
        return True
    except ValueError:
        return False


def build_download_url(file_path: str | Path) -> str:
    """Public URL for a file that lives inside REPORTS_DIR or PRESENTATIONS_DIR."""
    p = Path(file_path).resolve()
    base = Config.PUBLIC_BASE_URL.rstrip("/")
    if _is_within(p, Config.REPORTS_DIR.resolve()):
        return f"{base}{_REPORTS_PREFIX}/{quote(p.name)}"
    if _is_within(p, Config.PRESENTATIONS_DIR.resolve()):
        return f"{base}{_PRESENTATIONS_PREFIX}/{quote(p.name)}"
    raise ValueError(f"Path not in allowed download roots: {p}")


def register_download_routes(mcp) -> None:
    """Mount StaticFiles for the two output directories onto the FastMCP HTTP app."""
    Config.REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    Config.PRESENTATIONS_DIR.mkdir(parents=True, exist_ok=True)

    mcp._additional_http_routes.append(
        Mount(
            _REPORTS_PREFIX,
            app=StaticFiles(directory=str(Config.REPORTS_DIR), check_dir=False),
            name="reports",
        )
    )
    mcp._additional_http_routes.append(
        Mount(
            _PRESENTATIONS_PREFIX,
            app=StaticFiles(directory=str(Config.PRESENTATIONS_DIR), check_dir=False),
            name="presentations",
        )
    )
