import resend
import base64
import os
from dotenv import load_dotenv

load_dotenv()

resend.api_key = os.getenv("RESEND_API_KEY")

name = "Tatiana Paucar"
role = "AI Engineer Intern"
logo_url = "https://res.cloudinary.com/dqgpis4fg/image/upload/v1777557074/skptrceca3cyqlv5xspo.png"
from_email = "onboarding@resend.dev"
    

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
def encode_attachment(attachments: list[str]) -> list[dict]:
    resend_attachments = []
    for path in attachments:
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: {path}")

        with open(path, "rb") as f:
            resend_attachments.append({
                "filename": os.path.basename(path),
                "content": base64.b64encode(f.read()).decode("utf-8"),
            })  
    
    return resend_attachments
        

def send_email(
    to: str,
    subject: str,
    body: str,
    cc: list[str] | None = None,
    bcc: list[str] | None = None,
    attachments: list[str] | None = None,
) -> str:
    
    if not to or not subject or not body:
        raise ValueError("To, subject, and body are required fields.")
    
    payload = {
        "from": from_email,
        "to": [to],
        "subject": subject,
        "html": build_email_html(body, name, role, logo_url),
    }
    
    if cc:
        payload["cc"] = cc
        
    if bcc:
        payload["bcc"] = bcc
        
    if attachments:
        payload["attachments"] = encode_attachment(attachments)
        
     
    try: 
        email = resend.Emails.send(payload)
        return f"Email with attachment sent to {to}, id: {email.id}"
    except Exception as e:
        return f"Error sending email: {e}"    
    
    
    