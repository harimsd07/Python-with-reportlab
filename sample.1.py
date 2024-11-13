from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet

# Create a canvas object with the desired page size
c = canvas.Canvas("example.pdf", pagesize=letter)

# Set the font style and size
style = getSampleStyleSheet()["Normal"]
style.fontName = "Helvetica"
style.fontSize = 

# Set the coordinates for the text
x = 100
y = 100

# Draw the text
c.setFont(style.fontName, style.fontSize)
c.drawString(x, y, "Hello, World!")

# Save the canvas to a file or show it
c.save()
