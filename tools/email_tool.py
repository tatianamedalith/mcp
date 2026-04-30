import resend
import os
from dotenv import load_dotenv

load_dotenv()

resend.api_key = os.getenv("RESEND_API_KEY")


def send_email(to:str, subject:str, body:str):
    
    email = resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": [to],
        "subject": subject,
        "html": body,
    })
    return f"Email sent to {to}, id: {email.id}"

