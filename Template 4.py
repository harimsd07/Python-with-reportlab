from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors

def line(obj):
    obj.setLineWidth(5)
    obj.setStrokeColorRGB(0,0,0)
    obj.line(30,30,140,150)
    obj.line(470,150,580,30)
    obj.line(30,770,140,650)
    obj.line(470,650,580,770)
    obj.rect(30,30,550,740)
    #obj.setStrokeColorRGB(1,0,1)
    
    obj.rect(140,150,330,500)
   

if __name__=="__main__":
    obj=canvas.Canvas("Templete 4.pdf",pagesize=letter,bottomup=0)
    line(obj)
    obj.save()
    print("Pdf Generated")
