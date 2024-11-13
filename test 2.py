from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph, Frame,Spacer,SimpleDocTemplate,Image
from reportlab.rl_config import defaultPageSize

def newsPpr(obj):
    styles=getSampleStyleSheet()
    flowables=[]
    spacer=Spacer(1,0.1*inch)
    title="M.S.Dhoni"
    img=Image("Dhoni.jpg",2*inch,2*inch)
    flowables.append(spacer)
    flowables.append(img)
    flowables.append(Paragraph(title,styles["Heading1"]))
    flowables.append(spacer)
    text="M.S. Dhoni, in full Mahendra Singh Dhoni, (born July 7, 1981, Ranchi, Bihar [now Jharkhand] state, India), Indian cricketer whose rise to prominence in the early 21st century culminated in his captaincy of the Indian national team that won the one-day Cricket World Cup in 2011.Dhoni made his international debut in 2004. His talent with the bat came to the fore in an innings of 148 runs against Pakistan in his fifth international match. Within a year he joined the India Test team, where he quickly established himself with a century (100 or more runs in a single innings) against Pakistan. Despite his inexperience, Dhoni took over the captaincy of the one-day side in 2007 and led India to the Twenty20 (T20) world title"
    flowables.append(Paragraph(text,styles["Normal"]))
    left_frame=Frame(inch,inch,width=3*inch,height=7*inch,showBoundary=1)
    left_frame.addFromList(flowables,obj)
    
if __name__=="__main__":
    obj=canvas.Canvas("NewsPaper.pdf",pagesize=letter)
    newsPpr(obj)
    obj.save()
    print("Pdf Generated")
