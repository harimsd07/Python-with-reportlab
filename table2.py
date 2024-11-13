from reportlab.platypus import SimpleDocTemplate,Table,TableStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors

def fortable():

    doc=SimpleDocTemplate("second table.pdf",pagesize=letter)
    emplist=[]

    data=['col_{}'.format(x) for x in range(1, 6)],[str(x) for x in range(1, 6)],['a', 'b', 'c', 'd', 'e']
    tblstyle=TableStyle([("BACKGROUND",(0,1),(4,0),colors.red),("TEXTCOLOR",(0,1),(-1,1),colors.blue)])

    tblobj=Table(data)
    tblobj.setStyle(tblstyle)
    emplist.append(tblobj)
    doc.build(emplist)

if __name__=="__main__":
          fortable()
          print("PDF Generated")
