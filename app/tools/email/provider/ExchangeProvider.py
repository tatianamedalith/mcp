

import os
from exchangelib import DELEGATE, Account, Credentials, FileAttachment, HTMLBody, Mailbox, Message
from app.tools.email.provider.EmailProvider import EmailProvider


class ExchangeProvider(EmailProvider):
    def send(self, to, subject, html, cc, bcc, attachments) -> str:

        credentials = Credentials(
            username=os.getenv("EXCHANGE_USER", ""),
            password=os.getenv("EXCHANGE_PASSWORD", ""),
        )
        account = Account(
            primary_smtp_address=os.getenv("EXCHANGE_EMAIL", ""),
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
            if not os.path.exists(path):
                raise FileNotFoundError(f"Attachment not found: {path}")
            with open(path, "rb") as f:
                msg.attach(FileAttachment(name=os.path.basename(path), content=f.read()))

        msg.send()
        return f"Email sent to {to} via Exchange"
