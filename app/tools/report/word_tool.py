from pathlib import Path

from docx import Document


def create_report(title: str, content: str, filename: str, output_path: str | None = None) -> str:
    base = Path(output_path) if output_path else Path("output")
    base.mkdir(parents=True, exist_ok=True)
    output = base / f"{filename}.docx"
    
    doc = Document()
    doc.add_heading(title, level=1)
    doc.add_paragraph(content)
    doc.save(output)
    
    return str(output.resolve()) 
