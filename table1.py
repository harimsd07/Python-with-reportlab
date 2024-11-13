from reportlab.platypus import SimpleDocTemplate,Table
from reportlab.lib.pagesizes import letter

def simpletable():
    doc_obj=SimpleDocTemplate("Just a table.pdf",pagesize=letter)
    emplist=[]

    data =[['col_{}'.format(x) for x in range(1, 18)],[str(x) for x in range(1, 18)],[chr(x) for x in range(97,115)]]
    tbl_obj=Table(data,rowSplitRange=5,rowHeights=30,colWidths=30,repeatRows=1)
    print(tbl_obj)
    emplist.append(tbl_obj)
    doc_obj.build(emplist)

if __name__=="__main__":
    simpletable()
    print("pdf generated")
        
