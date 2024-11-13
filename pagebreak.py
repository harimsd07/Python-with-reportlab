from reportlab.platypus import SimpleDocTemplate,Paragraph,PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

def pagebreak():
    doc =SimpleDocTemplate("Pagebreak.pdf",pagesize=letter)
    styles=getSampleStyleSheet()
    emptylist=[]

    text=" I am IRAH "
    emptylist.append(Paragraph(text,style=styles["Code"]))
    pagebreak=PageBreak()
    emptylist.append(PageBreak())

    text=" I am IRAH "
    emptylist.append(Paragraph(text,style=styles["Code"]))

    doc.build(emptylist)

if __name__=="__main__":
    pagebreak()
    print("PDF Generated")
    
