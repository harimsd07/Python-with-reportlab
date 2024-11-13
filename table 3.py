from reportlab.lib import colors
from reportlab.platypus import Table ,TableStyle,SimpleDocTemplate,Spacer
from reportlab.lib.pagesizes  import letter

def twotable():
    doc=SimpleDocTemplate("Table3.pdf",pagesize=letter)
    emptylist=[]

    data=[["colm-{}".format(x) for x in range(0,6)],[str(x) for x in range(0,6)],['a','b','c','d','e','f']]
    tblstyle = TableStyle(
            [('LINEABOVE', (0, 0), (-1, 0), 0.5, colors.red),
             ('LINEBELOW', (0, 0), (-1, 0), 1.5, colors.blue),
             ('LINEBEFORE', (0, 0), (0, -1), 2.5, colors.orange),
             ('LINEAFTER', (0, 0), (4, 2), 3.5, colors.green),
            ])
    tbl=Table(data)
    tbl.setStyle(tblstyle)
    emptylist.append(tbl)
    emptylist.append(Spacer(0,25))

    tbl=Table(data , style=[("GRID",(0,0),(5,2),1,colors.red)])
    emptylist.append(tbl)
    doc.build(emptylist)


if __name__=="__main__":
          twotable()
          print("PDF generated")
          
