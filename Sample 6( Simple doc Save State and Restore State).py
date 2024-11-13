from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph

def create_first_page(canvas, doc):
    # Add custom content to the first page
    canvas.drawString(100, 700, "First Page")

def create_later_pages(canvas, doc):
    x=100
    y=700
    # Add custom content to subsequent pages
    for i in range(30):
        canvas.drawString(x, y, "Subsequent Page")
        y-=30
    

# Create a SimpleDocTemplate object
doc = SimpleDocTemplate("output.pdf", pagesize=letter)

# Define the document content as flowables
content = [
    Paragraph("Hello, World!", style=None),
    # ... add more paragraphs or other flowable elements ...
]

# Build the document with custom page functions
doc.build(flowables=content, onFirstPage=create_first_page, onLaterPages=create_later_pages)
