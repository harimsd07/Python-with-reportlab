from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph,Preformatted,XPreformatted
from reportlab.platypus import SimpleDocTemplate,Spacer,Frame
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

def paragraph(canvas):
    doc=SimpleDocTemplate("formated.pdf",pagesize=letter)
    styles=getSampleStyleSheet()
    emptylist=[]

    frame=Frame(30,150,120,450,showBoundary=1)
    frame.addFromList(emptylist,canvas)

    text="""The maxLineLength argument is used to define the maximum line length
 allowed in the Flowable. If your text happens to exceed the length that you
 define, the line will be automatically split."""
    para=Preformatted(text,style=styles["Code"],maxLineLength=80)
    emptylist.append(para)
    emptylist.append(Spacer(0,20))

   
    doc.build(emptylist)

if __name__=="__main__":
    paragraph(canvas)
    print("PDF Generated")
