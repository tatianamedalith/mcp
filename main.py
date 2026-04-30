from tools.email_tool import send_email
from tools.word_tool import create_word
from tools.slides_tool import create_presentation
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("lexi")

@mcp.tool()
def email(to:str, subject:str, body:str):
    """
    Send an email to the specified recipient.

    Parameters:
    - to: The email address of the recipient.
    - subject: The subject of the email.
    - body: The body content of the email.

    Returns:
    A confirmation message indicating that the email has been sent.
    """
    return send_email(to, subject, body)

@mcp.tool()
def word(title: str, content: str, filename: str) -> str:
    """
    Create a Word document with the given title and content, and save it with the specified filename.

    Parameters:
    - title: The title of the Word document.
    - content: The content to be included in the Word document.
    - filename: The name of the file to save the Word document as.

    Returns:
    A confirmation message indicating that the Word document has been created.
    """
    return create_word(title, content, filename)

@mcp.tool()
def presentation(title: str, slides: str, filename: str) -> str:
    """
    Crea una presentación PowerPoint.

    Parameters:
    - title: Título de la presentación
    - slides: Slides separadas por '|'. Ejemplo: "Título:Contenido|Título2:Contenido2"
    - filename: Nombre del archivo sin .pptx
    """
    return create_presentation(title, slides, filename)

def main():
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()

