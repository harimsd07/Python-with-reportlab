from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
def rect(obj):
    b=750
    x=30
    y=750
    for i in range(1,21):
        obj.drawString(10,b,str(i)+".")
        obj.rect(x,y,60,25)
        y-=35.5
        b-=35
    x=250
    y=750
    b=750
    for i in range(21,41):
        obj.drawString(228,b,str(i)+".")
        obj.rect(x,y,60,25)
        y-=35.5
        b-=35
    x=500
    y=750
    b=750
    for i in range(41,51):
        obj.drawString(474,b,str(i)+".")
        obj.rect(x,y,60,25)
        y-=35.5
        b-=35
if __name__=="__main__":
    obj=canvas.Canvas("rect33.pdf")
    rect(obj)
    print("pdf generated")
    obj.save()
