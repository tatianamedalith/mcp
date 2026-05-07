from html import escape


def build_html(
    body: str,
    sender_name: str,
    sender_role: str,
    sender_company: str,
) -> str:
    formatted = body.replace("\n", "<br>")
    name = escape(sender_name)
    role = escape(sender_role)
    company = escape(sender_company)
    return f"""
    <html>
        <body style="font-family: Arial, sans-serif; padding: 20px;">
            <p>{formatted}</p>
            <hr style="border: none; border-top: 1px solid #ccc; margin: 20px 0;">
            <p style="margin: 4px 0;">Saludos cordiales,</p>
            <p style="margin: 4px 0;"><strong>{name}</strong></p>
            <p style="margin: 4px 0;">{role}</p>
            <p style="margin: 4px 0; color: #555;">{company}</p>
        </body>
    </html>
    """
