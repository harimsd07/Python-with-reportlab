from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm

def draw_line(a):
  a.setLineWidth(5)
  a.line(10,50,10,150)



if __name__=='_main_':
  a= canvas.Canvas("lines.pdf",bottomup=0)
  draw_line(a)
  a.showPage()
  a.save()



