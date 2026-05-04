from dotenv import load_dotenv

from .template.default import build_html
from .provider.SmtpProvider import SmtpProvider
from .provider.ExchangeProvider import ExchangeProvider

load_dotenv()

_provider = SmtpProvider()  # swap to ExchangeProvider() for Outlook


def send_email(
    to: list[str],
    subject: str,
    body: str,
    cc: list[str] | None = None,
    bcc: list[str] | None = None,
    attachments: list[str] | None = None,
) -> str:
  
    if not to or not subject or not body:
        raise ValueError("to, subject, and body are required.")
    try:
        return _provider.send(to, subject, build_html(body), cc or [], bcc or [], attachments or [])
    except Exception as e:
        return f"Error sending email: {e}"
