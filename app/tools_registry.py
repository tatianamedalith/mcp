from fastmcp import FastMCP

from app.config import Config
from app.tools.email import send_email as _send_email
from app.tools.report.word_tool import create_report as _create_report
from app.tools.presentation.slides_tool import create_presentation as _create_presentation
from app.tools.task.task_tool import create_task, list_task, delete_task

mcp = FastMCP("lexi")


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
def create_report(
    title: str,
    content: str,
    filename: str,
    sections: str | None = None,
    output_path: str | None = None,
) -> str:
    """
    Create a Word document (.docx) with optional sections.
    
    Args:
        title: Main title of the document.
        content: Introductory body text (plain text).
        filename: Desired output filename (without .docx extension).
        sections: Optional pipe-separated section blocks in the format "SectionTitle:SectionContent".
                  Example: "Summary:Key findings|Details:Full analysis"
        output_path: Optional absolute folder path where the file will be saved.
                     Defaults to Config.REPORTS_DIR.
    
    Returns:
        Absolute path of the created .docx file.
    """
    return _create_report(
        title, content, filename,
        sections=sections,
        output_path=output_path or str(Config.REPORTS_DIR),
    )


@mcp.tool()
def create_presentation(title: str, slides: str, filename: str, output_path: str | None = None) -> str:
    """
    Create a PowerPoint presentation (.pptx) from a template.
    
    The template has two slides: a title slide and a content slide.
    The title slide is updated with the given title.
    The content slide is multiplied (one per slide entry) and each copy is filled with the provided data.
    
    Args:
        title: Presentation title (used on the first/title slide).
        slides: Pipe-separated slide definitions in the format "Title:Content" or "Title:Content:image_path".
                Example: "Intro:Welcome|Chart:Q1 results:/reports/chart.png"
                - Title: section title (appears as slide heading)
                - Content: body text (plain)
                - image_path: optional absolute path to an image (jpg, png, etc.)
        filename: Desired output filename (without .pptx extension).
        output_path: Optional absolute folder path where the file will be saved.
                     Defaults to Config.PRESENTATIONS_DIR.
    
    Returns:
        Absolute path of the created .pptx file.
    """
    
    return _create_presentation(title, slides, filename, output_path=output_path or str(Config.PRESENTATIONS_DIR))

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
