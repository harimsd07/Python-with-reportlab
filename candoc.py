from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

c=canvas.Canvas("pdf.pdf",pagesize=letter)

c.drawString(100, 700, "Hello, World!")
c.setStrokeColorRGB(0.2, 0.4, 0.6)
c.rect(100, 600, 200, 100, fill=1)
c.drawImage("Apple.jpg", 100, 400, width=200, height=200)

doc=SimpleDocTemplate("Pdf.pdf")
styles = getSampleStyleSheet()
flowables = []
text = "This is some sample text."
para = Paragraph(text, styles["Normal"])
flowables.append(para)

def draw_canvas(canvas_obj):
    canvas_obj.showPage()
    canvas_obj.save()
    flowables.append(canvas_obj)

draw_canvas(c)
doc.build(flowables)
print("Pdf Generated")
