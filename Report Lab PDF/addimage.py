from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def image(path):
    o=canvas.Canvas("phoyo.pdf",bottomup=1,pagesize=letter)
    o.drawImage(path,100,200,60,120)
    o.save()
print("moon.png")

if __name__=='__main__':
    path="moon.png"
    image(path)
