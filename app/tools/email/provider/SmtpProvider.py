
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import make_msgid
import smtplib
from app.tools.email.provider.EmailProvider import EmailProvider
from app.config import Config
import os

class SmtpProvider(EmailProvider):
    def send(self, to, subject, html, cc, bcc, attachments) -> str:
        user = Config.SMTP_USER
        password = Config.SMTP_PASSWORD
        from_addr = user
        host = Config.SMTP_HOST
        port = Config.SMTP_PORT

        msg_id = make_msgid(domain=user.split("@")[-1] if "@" in user else "local")
        mime = self._build_mime(to, subject, html, from_addr, cc, attachments, msg_id)

        with smtplib.SMTP(host, port) as server:
            server.starttls()
            server.login(user, password)
            server.sendmail(from_addr, to + cc + bcc, mime.as_string())

        return f"Email sent to {to} via SMTP, message_id: {msg_id}"

    def _build_mime(self, to, subject, html, from_addr, cc, attachments, msg_id) -> MIMEMultipart:
        if attachments:
            outer = MIMEMultipart("mixed")
            body_part = MIMEMultipart("alternative")
            body_part.attach(MIMEText(html, "html"))
            outer.attach(body_part)
            for path in attachments:
                outer.attach(self._encode_file(path))
        else:
            outer = MIMEMultipart("alternative")
            outer.attach(MIMEText(html, "html"))

        outer["Subject"] = subject
        outer["From"] = from_addr
        outer["To"] = ", ".join(to)
        outer["Message-ID"] = msg_id
        if cc:
            outer["Cc"] = ", ".join(cc)
        return outer

    def _encode_file(self, path: str) -> MIMEBase:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Attachment not found: {path}")
        part = MIMEBase("application", "octet-stream")
        with open(path, "rb") as f:
            part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f'attachment; filename="{os.path.basename(path)}"')
        return part