
from exchangelib import DELEGATE, Account, Credentials, FileAttachment, HTMLBody, Mailbox, Message
from pathlib import Path

from app.tools.email.provider.EmailProvider import EmailProvider
from app.config import Config


class ExchangeProvider(EmailProvider):
    def send(self, to, subject, html, cc, bcc, attachments) -> str:

        credentials = Credentials(
            username=Config.EXCHANGE_EMAIL,
            password=Config.EXCHANGE_PASSWORD,
        )
        account = Account(
            primary_smtp_address=Config.EXCHANGE_EMAIL,
            credentials=credentials,
            autodiscover=True,
            access_type=DELEGATE,
        )

        msg = Message(
            account=account,
            subject=subject,
            body=HTMLBody(html),
            to_recipients=[Mailbox(email_address=addr) for addr in to],
            cc_recipients=[Mailbox(email_address=addr) for addr in cc],
            bcc_recipients=[Mailbox(email_address=addr) for addr in bcc],
        )

        for path in attachments:
            p = Path(path)
            if not p.exists():
                raise FileNotFoundError(f"Attachment not found: {path}")
            msg.attach(FileAttachment(name=p.name, content=p.read_bytes()))

        msg.send()
        return f"Email sent to {to} via Exchange, message_id: {msg.message_id}"
