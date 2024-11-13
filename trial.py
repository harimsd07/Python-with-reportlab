from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Frame, PageTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Create the document and specify the page size
doc = SimpleDocTemplate("combined_frames.pdf", pagesize=letter)

# Define the frames for your layout
frame1 = Frame(30,40 , 150,200, id='frame1',showBoundary=1)
frame2 = Frame(200, 40, 150,200, id='frame2',showBoundary=1)
print(frame1)

# Create a PageTemplate with the defined frames
page_template = PageTemplate(id='two_column_template', frames=[frame1, frame2])

# Add the PageTemplate to the document
doc.addPageTemplates(page_template)

# Create sample content for each frame
content_frame1 = "This is content for Frame 1"
content_frame2 = "This is content for Frame 2"

# Create Paragraphs for each content
styles = getSampleStyleSheet()
paragraph_frame1 = Paragraph(content_frame1, styles['Normal'])
paragraph_frame2 = Paragraph(content_frame2, styles['Normal'])

# Build the document and add the content to the corresponding frames
story = [paragraph_frame1 , paragraph_frame2]
doc.build(story)
