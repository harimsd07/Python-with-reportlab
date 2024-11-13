from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Image
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.units import inch
import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import utils

def simple():
    x=30
    y=70
    doc=SimpleDocTemplate("Design.pdf")
    styles = getSampleStyleSheet()
    flowables=[]
    formatted_time=time.ctime()
    name="Irah"
    num=15
    img=Image("Anna University logo.jpg",2*inch,2*inch)
    flowables.append(img)
    flowables.append(Spacer(1,15))
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    ptext = '<font size=12>%s</font>' % formatted_time
    flowables.append(Paragraph(ptext,styles["Normal"]))
    flowables.append(Spacer(1,15))
    ptext = '<font size=12>%d</font>' % num
    flowables.append(Paragraph(ptext,styles["Normal"]))
    flowables.append(Spacer(1,15))
    
    
    doc.build(flowables)
    
if __name__=='__main__':
    simple()
    print("PDF Generated")
