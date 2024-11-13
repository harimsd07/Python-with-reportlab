from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors


def margin(obj):
    obj.roundRect(30,30,540,740,50)


def page(obj):
    obj.setFont("Courier",20)
    obj.saveState()
    obj.drawString(90,90,"Hell0")
    obj.setFont("Helvetica",20)
    obj.drawString(90,150,"Hell0")
    obj.restoreState()
    obj.drawString(90,180,"Hell0")
    obj.setFont("Times-Italic",20)
    obj.drawString(90,210,"Hell0")
    obj.saveState()
    obj.drawString(90,240,"Irah")
    obj.restoreState()
    obj.drawString(90,270,"Irah")


if __name__ == "__main__":

    obj = canvas.Canvas("example_pdf.pdf",letter,bottomup=0)
    page(obj)
    margin(obj)
    print("PDF Generated")
    obj.save()
