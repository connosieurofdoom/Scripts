# Read and Create PDF
# pip install PyMuPDF
# pip install fpdf2
# Read PDF file
import fitz
def read_pdf(file_name):
    pdf = fitz.open(file_name)
    text = ""
    for p in pdf:
        text += p.getText()
    return text

# Write PDF file
import fpdf
def write_pdf():
    PDF_w = fpdf.FPDF()
    PDF_w.add_page()
    PDF_w.set_font("Arial", size=12)
# Single cell
    PDF_w.cell(txt="Hello Medium World", )
    
    # Multi Cell
    PDF_w.multi_cell(0, 5, "Hello Medium World")
    PDF_w.output("my_test.pdf")