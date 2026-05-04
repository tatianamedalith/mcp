from mcp.server.fastmcp import FastMCP

from app.tools.email import send_email as _send_email
from app.tools.report.word_tool import create_report as _create_report
from app.tools.presentation.slides_tool import create_presentation as _create_presentation

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
