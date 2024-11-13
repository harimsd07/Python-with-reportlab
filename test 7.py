from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph,Frame,KeepInFrame
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas

obj=canvas.Canvas("Combining Frames.pdf",pagesize=letter)
emptyframe=[]
styles=getSampleStyleSheet()
style=styles["Normal"]
paragraph=Paragraph("Scikit-learn is simple to work with and delivers successful performance. Scikit Learn, though, does not enable parallel processing. We can implement deep learning algorithms in sklearn, though it is not a wise choice, especially if using TensorFlow is an available option.",style)
frame1=Frame(30,400,400,50,showBoundary=1)
frame2=Frame(30,340,400,50,showBoundary=1)

lines=frame1.split(paragraph,style)
#print(lines)
paragraph1=Paragraph(lines,style)
print(paragraph1)
emptyframe.append(paragraph1)
#keepframe=KeepInFrame(400,50,[paragraph])
#emptyframe.append(keepframe)
print(frame)
#print(keepframe)
frame.addFromList(emptyframe,obj)
#doc.addPageTemplate([frame])
obj.save()
