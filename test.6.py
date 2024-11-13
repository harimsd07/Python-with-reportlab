from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
def generate_pdf():
    doc = SimpleDocTemplate("output.pdf", pagesize=letter)
    story = []
    
    # Get the current date and format it
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # Create a paragraph with the date
    styles = getSampleStyleSheet()
    date_text = "<b>Date:</b> {}".format(current_date)
    paragraph = Paragraph(date_text, styles["Normal"])
    
    # Add the paragraph to the story
    story.append(paragraph)
    
    # Build the PDF document
    doc.build(story)
generate_pdf()
