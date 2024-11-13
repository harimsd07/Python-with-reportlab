from reportlab.platypus import SimpleDocTemplate,Paragraph,PageBreak
from reportlab.platypus.tableofcontents import SimpleIndex
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet

def simpleindex():

    doc = SimpleDocTemplate("simple_index1.pdf",pagesize=letter)
    styles = getSampleStyleSheet()
    flowables = []
    ptext = """I'm a custom <index item="bulletted"/>bulletted paragraph"""
    para = Paragraph(ptext, style=styles["Normal"], bulletText='-')
    flowables.append(para)
    flowables.append(PageBreak())
    
    ptext = """<index item="Python"/>Python is an indexed word"""
    para = Paragraph(ptext, style=styles["Normal"], bulletText='-')
    flowables.append(para)
    flowables.append(PageBreak())
    
    ptext = """I'm a custom <index item="bulletted"/>bulletted paragraph"""
    para = Paragraph(ptext, style=styles["Normal"], bulletText='-')
    flowables.append(para)
    flowables.append(PageBreak())
     
    ptext = """<index item="foo,bar,word"/>this is index item test"""
    para = Paragraph(ptext, style=styles["Normal"], bulletText='-')
    flowables.append(para)
    flowables.append(PageBreak())

    ptext = """<index item="just testing,result the test"/>this is another index item test"""
    para = Paragraph(ptext, style=styles["Normal"], bulletText='-')
    flowables.append(para)
    
    index = SimpleIndex()
    print(index)
    flowables.append(PageBreak())
    flowables.append(index)
    doc.build(flowables,canvasmaker=index.getCanvasMaker())
    #print(doc.build(flowables,canvasmaker=index.getCanvasMaker()))

if __name__=="__main__":
    simpleindex()
    print("PDF Generated")
