from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Image, Spacer

# Define the PDF document size and margins
PAGE_WIDTH, PAGE_HEIGHT = letter
MARGIN = inch

# Create a new PDF document
pdf = SimpleDocTemplate('example.pdf', pagesize=letter)

# Set the document styles
styles = getSampleStyleSheet()

# Create a flowables list
flowables = []

def border(obj):
    obj.roundRect(30,30,540,720,50)
    obj.line(190,30,190,750)
    obj.line(380,30,380,750)
    obj.line(30,250,570,250)
    obj.line(30,500,570,500)
    x=70
    y=600
    k=96
    
    
if __name__=="__main__":
    obj=canvas.Canvas("Template 3.pdf",pagesize=letter,bottomup=1)
    
    border(obj)
    print("Pdf Genrated")
    obj.showPage()
    obj.save()
    
