from fastmcp import FastMCP

from app.auth import token_verifier
from app.config import Config
from app.tools.email import send_email as _send_email
from app.tools.report.word_tool import create_report as _create_report
from app.tools.presentation.slides_tool import create_presentation as _create_presentation
from app.tools.task.task_tool import create_task, list_task, delete_task

mcp = FastMCP("lexi", auth=token_verifier)


@mcp.tool()
def send_email(
    to: list[str],
    subject: str,
    body: str,
    cc: list[str] | None = None,
    bcc: list[str] | None = None,
    attachments: list[str] | None = None,
) -> str:
    """
    Send an email.
    - to: recipient email addresses
    - subject: email subject
    - body: plain text body (wrapped in HTML template with signature)
    - cc: CC recipients (optional)
    - bcc: BCC recipients (optional)
    - attachments: absolute file paths to attach (optional)
    Returns a confirmation with message_id.
    """
    return _send_email(to, subject, body, cc=cc, bcc=bcc, attachments=attachments)


@mcp.tool()
def create_report(title: str, content: str, filename: str) -> str:
    """
    Create a Word document (.docx).
    - title: document title
    - content: body text
    - filename: output file name (without .docx)
    Returns the file name of the created document.
    """
    return _create_report(title, content, filename)


@mcp.tool()
def create_presentation(title: str, slides: str, filename: str) -> str:
    """
    Create a PowerPoint presentation (.pptx).
    - title: presentation title
    - slides: pipe-separated slides as 'Title:Content'
      Example: "Intro:Welcome|Overview:Key points"
    - filename: output file name (without .pptx)
    Returns the file name of the created presentation.
    """
    return _create_presentation(title, slides, filename)

@mcp.tool()
def manage_task(action: str, task_name: str, script_path: str = "", trigger_time: str = "08:00") -> str:
    """
    Manage Windows Task Scheduler tasks.
    - action: "create" | "list" | "delete"
    - task_name: unique task name
    - script_path: path to .py script (required for create)
    - trigger_time: "HH:MM" daily trigger (required for create)
    """
    config = {"task_manager": {"python_path": Config.PYTHON_PATH}}
    params = {"action": action, "task_name": task_name, "script_path": script_path, "trigger_time": trigger_time}

    if action == "create":
        return str(create_task(params, config))
    elif action == "list":
        return str(list_task())
    elif action == "delete":
        return str(delete_task(params))
    raise ValueError(f"Acción no válida: {action}")
