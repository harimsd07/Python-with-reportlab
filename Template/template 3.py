from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import red
from reportlab.lib.styles import getSampleStyleSheet

def border(obj,lst):
  
    x=70
    y=600
    k=96
    #second column
    a=250
    b=600
    c=0
    textcolor=red
    for i in range(9):
        obj.roundRect(30,30,540,720,50)
        obj.line(190,30,190,750)
        obj.line(380,30,380,750)
        obj.line(30,250,570,250)
        obj.line(30,500,570,500)
        for i in range(k+1,k+4,1):
            style=getSampleStyleSheet()
            style.fontName="Helvetica"
            style.fontSize=80
            obj.setFont(style.fontName,style.fontSize)
            obj.setFillColor(textcolor)
            obj.drawString(x,y,chr(i))
            y-=250
        x=70
        y=600
        for j in range(c,c+3,1):
            obj.drawImage(lst[j],a,b,100,100)
            b-=250
        a=250
        y=600
        
        k=i
        c=j
        obj.showPage()
        #print(j)
        
        
       
if __name__=="__main__":
    obj=canvas.Canvas("Template 3.pdf",pagesize=letter,bottomup=1)
    lst=["Aeroplane.png","Banana.jpg","cat.jpg","Dog.jpg","Eagle.jpg","Fruits.png","Goat.jpg","Hat.png","Ice.jpg","Joker.jpg","Kite.jpg","Lion.jpg","Mango.jpg","Needle.jpg","Orange.jpg","Pig.jpg","Quill.jpg","Rabbit.jpg","Sun.jpg","Train.jpg","Umberlla.jpg","Violin.jpg","Watch.jpg","Xylophone.jpg","Yacht.jpg","Zebra.jpg"]
    border(obj,lst)
    obj.save()
    print("Pdf Generated")
    
