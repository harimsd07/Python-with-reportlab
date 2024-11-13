from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Image
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet

def first_page(canvas,document):
    title="ANIME REVIEW"
    PAGE_HIEGHT=defaultPageSize[1]
    PAGE_WIDTH=defaultPageSize[0]
    print(PAGE_HIEGHT)
    print(PAGE_WIDTH)
    canvas.saveState()
    #canvas.setFont("Bold",12)
    canvas.drawCentredString(PAGE_WIDTH/2,PAGE_HIEGHT-108,title)
    canvas.restoreState()
def later_pages(canvas,document):
    canvas.saveState()
    canvas.drawString(7*inch,0.3*inch,"Page{}".format(document.page))
    canvas.restoreState()
def sample():
    doc= SimpleDocTemplate("Simple Doc.pdf",pagesize=letter)
    styles=getSampleStyleSheet()
    flowable=[]
    spacer=Spacer(1,0.7*inch)
    text="NARUTO "
    flowable.append(spacer)
   
    pic="NARUTO( FLOWABLES EX -1).jpg"
    img=Image(pic,5*inch,5*inch)
    para=Paragraph(text,styles["Normal"])
    flowable.append(para)
    flowable.append(spacer)
    flowable.append(img)
    flowable.append(spacer)
    text1=["Naruto Uzumaki, a mischievous adolescent ninja, struggles as he searches for recognition and dreams of becoming the Hokage, the village's leader and strongest ninja","Creator:-Masashi Kishimoto","It was a life changing anime for me, personally","Ït deal with,Love,Friendship,Foe,Loyalty,Determination,..."]   
    for i in text1:
        para=Paragraph(str(i),styles["Normal"])
        print(para)
        flowable.append(para)
    flowable.append(spacer)
    flowable.append(spacer)
    flowable.append(spacer)
    flowable.append(spacer)
    

    text2="ONE PIECE"
    pic2="ONE PIECE (Flowables EX-2).jpg"
    img2=Image(pic2,5*inch,5*inch)
    para=Paragraph(text2,styles["Normal"])
    flowable.append(para)
    flowable.append(spacer)
    flowable.append(img2)
    flowable.append(spacer)
    text3=["Follows the adventures of Monkey D. Luffy and his pirate crew in order to find the greatest treasure ever left by the legendary Pirate, Gold Roger"," The famous mystery treasure named ONE PIECE"," Creator:-Eiichirô Oda"]
    for j in text3:
        para=Paragraph(str(j),styles["Normal"])
        print(para)
        flowable.append(para)
    flowable.append(spacer)
    doc.build(flowable,onFirstPage=first_page,onLaterPages=later_pages)
    
if __name__=="__main__":
    sample()
    print("Pdf Generated")
