from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
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

# Add a title to the document
title = Paragraph('<h1>Example PDF Document</h1>')
flowables.append(title)

# Add an image to the document
image = Image('RAM.jpg', width=4*inch, height=3*inch)
flowables.append(image)

# Add some text to the document
text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed convallis mauris sapien, eu suscipit est ullamcorper eu. Nulla tristique dolor et metus ultrices, vel egestas augue interdum. Integer ullamcorper blandit nisl vel bibendum. Donec auctor, ex in bibendum dictum, sapien augue tincidunt quam, vel elementum elit elit eu nisi. Nulla at lacus ultricies, interdum mi in, venenatis tellus. Etiam molestie magna in tellus hendrerit, vel facilisis leo rhoncus.
"""
paragraph = Paragraph(text, styles['Normal'])
flowables.append(paragraph)

# Add some white space to the document
spacer = Spacer(1, 0.25*inch)
flowables.append(spacer)

# Draw a line in the document
pdf.line(MARGIN, PAGE_HEIGHT - MARGIN, PAGE_WIDTH - MARGIN, PAGE_HEIGHT - MARGIN)

# Build the document
pdf.build(flowables)
