from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph,Frame,SimpleDocTemplate
from reportlab.lib.pagesizes import letter,landscape
from reportlab.lib.styles import getSampleStyleSheet

def body_of_page(canvas,doc):
    canvas.roundRect(30,30,540,780,50)
    title1 = 'TECH'
    title2 = 'TODAY'
    PAGE_HEIGHT = defaultPageSize[1] #841.8897
    PAGE_WIDTH = defaultPageSize[0]#595.2755
    canvas.setFont("Courier-Bold",60)
    canvas.setFillColor(colors.red)
    canvas.drawCentredString(PAGE_WIDTH/3.8,PAGE_HEIGHT-90,title1)
    canvas.drawCentredString(PAGE_WIDTH/1.4,PAGE_HEIGHT-90,title2)  
    #obj.drawImage("Temp 5.jpg",PAGE_WIDTH/2.5,PAGE_HEIGHT-100,80,50)
    #top 
    canvas.line(30,740,570,740)
    #obj.line(180,810,180,740) #top vertical line1
    #obj.line(420,810,420,740) #top vertical line2
    #bottom
    canvas.line(30,70,570,70)
    canvas.line(180,70,180,30)
    canvas.line(420,70,420,30)
    doc.build(canvas) 
    

if __name__=="__main__":
    doc=SimpleDocTemplate("Article 1.pdf",pagesize=letter)
    body_of_page(doc,canvas)
    print("PDF Generated")
    
