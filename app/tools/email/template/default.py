NAME = "Tatiana Paucar"
ROLE = "AI Engineer Intern"
LOGO = "https://res.cloudinary.com/dqgpis4fg/image/upload/v1777557074/skptrceca3cyqlv5xspo.png"


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
