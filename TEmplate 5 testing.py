from reportlab.platypus import SimpleDocTemplate,Spacer,Paragraph,Frame
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib import colors
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
def first_page(canvas,document):
    canvas.roundRect(30,30,540,780,50)
    title1 = 'TECH'
    title2 = 'TODAY'
    PAGE_HEIGHT = defaultPageSize[1] #841.8897
    PAGE_WIDTH = defaultPageSize[0]#595.2755
    obj.setFont("Courier-Bold",60)
    canvas.setFillColor(colors.red)
    canvas.drawCentredString(PAGE_WIDTH/3.8,PAGE_HEIGHT-90,title1)
    canvas.drawCentredString(PAGE_WIDTH/1.4,PAGE_HEIGHT-90,title2)  
    canvas.drawImage("Temp 5 pic .png",PAGE_WIDTH/2.5,PAGE_HEIGHT-100,80,50)
    #top 
    canvas.line(30,740,570,740)
    #obj.line(180,810,180,740) #top vertical line1
    #obj.line(420,810,420,740) #top vertical line2
    #bottom
    canvas.line(30,70,570,70)
    canvas.line(180,70,180,30)
    canvas.line(420,70,420,30)

def create_document():
    doc=SimpleDocTemplate("Article 1.pdf",pagesize=letter)
    flowables=[]
    def first_page(canvas,document):
        canvas.roundRect(30,30,540,780,50)
        title1 = 'TECH'
        title2 = 'TODAY'
        PAGE_HEIGHT = defaultPageSize[1] #841.8897
        PAGE_WIDTH = defaultPageSize[0]#595.2755
        obj.setFont("Courier-Bold",60)
        canvas.setFillColor(colors.red)
        canvas.drawCentredString(PAGE_WIDTH/3.8,PAGE_HEIGHT-90,title1)
        canvas.drawCentredString(PAGE_WIDTH/1.4,PAGE_HEIGHT-90,title2)  
        canvas.drawImage("Temp 5 pic .png",PAGE_WIDTH/2.5,PAGE_HEIGHT-100,80,50)
        #top 
        canvas.line(30,740,570,740)
        #obj.line(180,810,180,740) #top vertical line1
        #obj.line(420,810,420,740) #top vertical line2
        #bottom
        canvas.line(30,70,570,70)
        canvas.line(180,70,180,30)
        canvas.line(420,70,420,30)
        flowables.append(canvas)
    doc.build(flowables,onFirstPage=first_page)
if __name__ =="__main__":
    create_document()
    print("PDF Generated")
