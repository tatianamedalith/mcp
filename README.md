# Lexi MCP Server

MCP server over streamable HTTP with JWT authentication and rate limiting.

## Tools

| Tool | Description |
|---|---|
| `send_email` | Send emails via SMTP or Exchange |
| `create_report` | Generate a Word document (.docx) |
| `create_presentation` | Generate a PowerPoint file (.pptx) |
| `manage_task` | Create, list, or delete Windows Task Scheduler tasks |

## Setup

```bash
git clone <repo>
cd mcp
uv sync
cp .env.example .env  # fill in your values
```


## Run

```bash
python -m app.main
```
