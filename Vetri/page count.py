from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

a= canvas.Canvas("nop3.pdf",bottomup=1)
a.drawString(10,810,"1 st page")
print("1 st page")
l=30
b=805
c=530
d=-760

def border():
    global l,b,c,d
    for i in range(4):
        a.rect(l,b,c,d)
        l+=30
        b-=30
        c-=60
        d+=60
    a.drawString(255,410,"border design")
        
if __name__=='__main__':
    border()
a.showPage()

#----- 2nd page------
a.drawString(10,810,"2 nd page")
print("2 nd page")
l=30
b=805
c=530
d=-760

def border():
    global l,b,c,d
    for i in range(4):
        a.rect(l,b,c,d)
        l+=30
        b-=30
        c-=60
        d+=60
    a.drawString(255,410,"border design")
        
if __name__=='__main__':
    border()
a.showPage()

#----- 3rd page -------
a.drawString(10,810,"3 rd page")
print("3 rd page")
l=30
b=805
c=530
d=-760

def border():
    global l,b,c,d
    for i in range(4):
        a.rect(l,b,c,d)
        l+=30
        b-=30
        c-=60
        d+=60
    a.drawString(255,410,"border design")
        
if __name__=='__main__':
    border()

a.save()
