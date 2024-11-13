from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch

print(inch)
page_height1= defaultPageSize[1]
page_height2= defaultPageSize[0]
print(page_height1)
print(page_height2)
page_width1= defaultPageSize[1]
page_widht2= defaultPageSize[0]
print(page_width1)
print(page_widht2)
print(getSpacerAfter())
