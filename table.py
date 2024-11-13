from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
def simple_table_with_style():
    doc = SimpleDocTemplate("rainbow table.pdf", pagesize=letter)
    story = []
    data = [['col_{}'.format(x) for x in range(1, 6)],[str(x) for x in range(1, 6)],['a', 'b', 'c', 'd', 'e'],["Hari","Hara","Sudhan","Irah","Nahdus"]]
    tblstyle = TableStyle([('BACKGROUND', (0, 0), (-1, 3),["HORIZONTAL",colors.red,colors.blue,colors.green,colors.orange,colors.yellow,colors.indigo,colors.violet]),('TEXTCOLOR', (0, 1), (-1, 1), colors.blue),("FONT",(0,3),(-1,3),"Helvetica",24)])
    tbl = Table(data)
    tbl.setStyle(tblstyle)
    story.append(tbl)
    doc.build(story)
if __name__ == '__main__':
    simple_table_with_style()
