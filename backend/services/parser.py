import fitz  # PyMuPDF
import docx

def extract_pdf(file_bytes):
    text = ""
    pdf = fitz.open(stream=file_bytes, filetype="pdf")
    
    for page in pdf:
        text += page.get_text()
    
    return text


def extract_docx(file_bytes):
    from io import BytesIO
    doc = docx.Document(BytesIO(file_bytes))
    
    return "\n".join([para.text for para in doc.paragraphs])
def clean_text(text):
    return text.replace("\n"," ").strip()