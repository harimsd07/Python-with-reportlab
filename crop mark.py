from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def fun(obj):
    obj.drawString(100,100,"The corpMark pdf")

if __name__=="__main__":
    obj=canvas.Canvas("1.pdf",cropMarks=True)
    fun(obj)
    obj.save()
