from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm

a=30
b=805
c=530
d=-760

def border_demo():
    global a,b,c,d
    for i in range(7):
        bor.rect(a,b,c,d)
        a+=30
        b-=30
        c-=60
        d+=60
    print("border")
    bor.drawString(255,410,"border design")


    bor.save()

if __name__=='__main__':
    bor=canvas.Canvas("border40.pdf",bottomup=1)
    border_demo()
