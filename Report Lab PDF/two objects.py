from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm

def drawcir(a,b):
    #a.drawString(100,100,"object 1")
    b.circle(100,600,60)
print("object 1 and a circle")





if __name__=='__main__':
    a= canvas.Canvas("two objects5.pdf",bottomup=1)
    b= canvas.Canvas("multi objects.pdf",bottomup=1)
    drawcir(a,b)
    a.save()
    b.save()
