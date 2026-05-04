from docx import Document


def create_report(title: str, content: str, filename: str, output_path: str | None = None) -> str:
    doc = Document()
    doc.add_heading(title, level=1)
    doc.add_paragraph(content)
    doc.save(filename)
    return f"Word document '{filename}' created successfully."
