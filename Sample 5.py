from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
def myFirstPage(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Bold',16)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, Title)
    canvas.setFont('Times-Roman',9)
    canvas.restoreState()

def create_pdf(sometext):
    doc = SimpleDocTemplate("myfile.pdf")
    Story = [Spacer(1,2*inch)]
    style = styles["Normal"]
    bogustext = ("There is something: %s. " % sometext)
    p = Paragraph(bogustext, style)
    Story.append(p)
    Story.append(Spacer(1,0.2*inch))
    doc.build(Story, onFirstPage=myFirstPage)
