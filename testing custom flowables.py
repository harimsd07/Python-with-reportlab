from Border import RectBorder
from reportlab.platypus import SimpleDocTemplate,Paragraph
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas


def box(canvas,document):
    doc =SimpleDocTemplate("Testing custom flowable.pdf",pagesize=letter)
    canvas.rect(30,30,540,740)
    border=RectBorder()
    print(border)
    styles=getSampleStyleSheet()
    print(styles)
    a=[]
    para=Paragraph("Welcome to the custom flowables",style=styles["Normal"])
    a.append(para)
    doc.build(a)
print("PDF Generated")
