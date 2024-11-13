from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors


def border(obj):
    obj.setLineWidth(10)
    obj.setStrokeColorRGB(0,0,1)
    obj.roundRect(30,30,550,730,30)#outer margin
    obj.roundRect(70,70,220,260,15)#bottom 1
    #obj.roundRect(73,73,210,250,13)
    obj.roundRect(340,70,220,260,15)#bottom 2
    #obj.roundRect(343,73,210,250,13)
    obj.roundRect(70,350,220,260,15)#3
    #obj.roundRect(73,353,210,250,13)
    obj.roundRect(340,350,220,260,15)#4
    #obj.roundRect(343,353,210,250,13)

def image(obj):    
        obj.drawImage("h.jpg",410,150,80,100)
        obj.drawImage("a.jpg",150,150,80,100)
        obj.drawImage("r.jpg",400,400,80,100)
        obj.drawImage("i.jpg",150,410,80,100)

def text(obj):
    obj.drawString(120,370,"Used to be introvert")
    obj.drawString(380,370,"Used to be rude")
    obj.drawString(120,120,"Used to be arrogant")
    obj.drawString(390,120,"at present always happy")
    
if __name__=="__main__":
    obj=canvas.Canvas("temp.pdf",pagesize=letter)
    border(obj)
    image(obj)
    text(obj)
    print("pdf generated")
    obj.save()
