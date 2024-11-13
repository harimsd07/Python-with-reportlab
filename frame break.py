from reportlab.platypus import SimpleDocTemplate,Frame,Paragraph,CondFrameBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def condbreak(doc,canvas):
    canvas.roundRect(30,30,540,720,50)
    styles=getSampleStyleSheet()
    emptylist=[]

    emptylist.append(Paragraph("Paragraph 1", styles["Normal"]))
    emptylist.append(CondFrameBreak(200))  # Add a frame break if 200 units of space are remaining in the frame
    emptylist.append(Paragraph("Paragraph 2", styles["Normal"]))
    frame.addFromList(emptylist,doc)
    doc.build(emptylist)


if __name__=="__main__":
    doc=SimpleDocTemplate("Framebreak.pdf",pagesize=letter)
    condbreak(doc)
    print("PDF Generated")
    
