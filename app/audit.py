import asyncio
import json
import sqlite3
import time
from datetime import datetime, timezone
from pathlib import Path

import mcp.types as mt
from fastmcp.server.middleware import CallNext, Middleware, MiddlewareContext
from fastmcp.server.middleware.middleware import ToolResult

DB_PATH = Path("audit.db")


def _init_db() -> None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS audit_log (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp   TEXT    NOT NULL,
                tool_name   TEXT    NOT NULL,
                arguments   TEXT,
                status      TEXT    NOT NULL,
                error       TEXT,
                duration_ms REAL
            )
        """)
        conn.commit()


_init_db()


async def _write(
    tool_name: str,
    arguments: dict | None,
    status: str,
    error: str | None,
    duration_ms: float,
) -> None:
    timestamp = datetime.now(timezone.utc).isoformat()
    args_json = json.dumps(arguments) if arguments else None

    def _sync() -> None:
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute(
                """INSERT INTO audit_log
                   (timestamp, tool_name, arguments, status, error, duration_ms)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (timestamp, tool_name, args_json, status, error, duration_ms),
            )
            conn.commit()

    await asyncio.to_thread(_sync)


class AuditMiddleware(Middleware):
    async def on_call_tool(
        self,
        context: MiddlewareContext[mt.CallToolRequestParams],
        call_next: CallNext,
    ) -> ToolResult:
        tool_name = context.message.name
        arguments = context.message.arguments
        start = time.perf_counter()

        try:
            result = await call_next(context)
            await _write(tool_name, arguments, "success", None, (time.perf_counter() - start) * 1000)
            return result
        except Exception as exc:
            await _write(tool_name, arguments, "error", str(exc), (time.perf_counter() - start) * 1000)
            raise
