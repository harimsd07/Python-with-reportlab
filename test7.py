from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
c = canvas.Canvas("draw_other.pdf")
c.ellipse(10, 60, 100, 100, stroke=1, fill=0)
c.save()
