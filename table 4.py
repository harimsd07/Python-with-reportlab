from reportlab.platypus import SimpleDocTemplate,Table,TableStyle
from reportlab.lib. pagesizes import letter
from reportlab.lib import colors

def func():
    doc = SimpleDocTemplate("Table 4.pdf",pagesize=letter)
    emptylist=[]

    data=[["colm-{}".format(x) for x in range(0,6)],[str(x) for x in range(0,6)],['a','b','c','d','e','f'],['a', 'b', 'c', 'd', 'e'],
    ['F', 'G', 'H', 'I', 'J']]
    print(len(data))
    tblstyle=([("INNERGRID",(0,0),(5,4),1,colors.red),("BOX",(0,0),(5,4),1,colors.orange),
               ("ALIGN",(0,0),(0,44),"CENTER"),
               ("ALIGN",(1,0),(1,4),"RIGHT"),
               ("VALIGN",(2,0),(2,4),"MIDDLE"),
               ("ALIGN",(2,0),(2,4),"CENTER")])
    tbl=Table(data,colWidths=[55 for x in range(5)],rowHeights=[45 for x in range(len(data))])
    tbl.setStyle(tblstyle)
    emptylist.append(tbl)
    doc.build(emptylist)

if __name__=="__main__":
    func()
    print("PDF Generated")
    
    
