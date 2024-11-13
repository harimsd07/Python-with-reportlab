from reportlab.pdfgen import  canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors

def template(obj):
    y=30
    obj.rect(30,30,540,740)
    for i in range(0,20,2):
        obj.setStrokeColorRGB(0,0,1)
    for i in range(20):
        obj.line(30,30,570,y)
        y+=20
    
if __name__=="__main__":
    obj=canvas.Canvas("template 2.pdf",pagesize=letter)
    template(obj)
    print("pdf generated")
    obj.save()
