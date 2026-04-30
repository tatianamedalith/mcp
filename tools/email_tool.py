import resend
import os
from dotenv import load_dotenv

load_dotenv()

resend.api_key = os.getenv("RESEND_API_KEY")


def build_email_html(body: str, name: str, role: str, logo_url: str) -> str:
    
    return f"""
    <html>
        <body style="font-family: Arial, sans-serif; padding: 20px;">
            <p>{body}</p>
            <hr style="border: none; border-top: 1px solid #ccc; margin: 20px 0;">
            <p style="margin: 4px 0;">Saludos cordiales,</p>
            <p style="margin: 4px 0;">{name}</p>
            <p style="margin: 4px 0;">{role}</p>
            <img src="{logo_url}" alt="iris" style="margin-top: 12px; width: 120px;">
        </body>
    </html>
    """

def send_email(to: str, subject: str, body: str) -> str:
    name = "Tatiana Paucar"
    role = "AI Engineer Intern"
    logo_url = "https://res.cloudinary.com/dqgpis4fg/image/upload/v1777557074/skptrceca3cyqlv5xspo.png"
    email = resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": [to],
        "subject": subject,
        "html": build_email_html(body, name, role, logo_url),
    })
    return f"Email sent to {to}, id: {email.id}"