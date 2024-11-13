from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate,paragraph
from reportlab.lib.styles import getsamplestylesheet


def sample():
    obj=SimpleDocTemplete("1 st try.pdf")
    
    styles= getSampleStyleSheet()
    print(getSampleStyleSheet())

    
if __name__=='__main__':
    sample()
