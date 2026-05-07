from .template.default import build_html
from .provider.SmtpProvider import SmtpProvider
from .provider.ExchangeProvider import ExchangeProvider
from app.config import Config

_provider = ExchangeProvider() if Config.EMAIL_PROVIDER.lower() == "exchange" else SmtpProvider()

def send_email(
    to: list[str],
    subject: str,
    body: str,
    sender_name: str,
    sender_role: str,
    sender_company: str,
    cc: list[str] | None = None,
    bcc: list[str] | None = None,
    attachments: list[str] | None = None,
) -> str:

    if not to or not subject or not body:
        raise ValueError("to, subject, and body are required.")
    if not sender_name or not sender_role or not sender_company:
        raise ValueError(
            "sender_name, sender_role and sender_company are required. "
            "The caller (LLM/user) must provide who is sending the email."
        )
    html = build_html(
        body,
        sender_name=sender_name,
        sender_role=sender_role,
        sender_company=sender_company,
    )
    try:
        return _provider.send(to, subject, html, cc or [], bcc or [], attachments or [])
    except Exception as e:
        return f"Error sending email: {e}"
