from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import letter


def shape_cir():
    q=canvas.Canvas("fullcir 8.pdf",bottomup=1)
    print(q)
    q.circle(400,800,100)
    q.circle(300,800,100)
    q.ellipse(10,780,100,730)
    q.showPage()
    q.save()
    
if __name__=='__main__':
    shape_cir()
