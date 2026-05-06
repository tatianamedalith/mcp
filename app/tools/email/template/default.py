from app.config import Config

NAME = Config.SIGNATURE_NAME
ROLE = Config.SIGNATURE_ROLE
LOGO = Config.SIGNATURE_LOGO

def build_html(body: str) -> str:
    return f"""
    <html>
        <body style="font-family: Arial, sans-serif; padding: 20px;">
            <p>{body}</p>
            <hr style="border: none; border-top: 1px solid #ccc; margin: 20px 0;">
            <p style="margin: 4px 0;">Saludos cordiales,</p>
            <p style="margin: 4px 0;">{NAME}</p>
            <p style="margin: 4px 0;">{ROLE}</p>
            <img src="{LOGO}" alt="logo" style="margin-top: 12px; width: 120px;">
        </body>
    </html>
    """
