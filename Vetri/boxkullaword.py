from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

naruto=[['N','A','R','U'],['H','I','N','A']]
x1=190
y1=255
print(naruto)

def draw_border(obj):
  obj.line(30,30,565,30)#upper 
  obj.line(30,30,30,775)#left
  obj.line(565,30,565,775)#right
  obj.line(30,775,565,775)#base
  
def draw_box(obj):
  x=180
  y=230
  b=30
  for i in range(x,480,30):
     for j in range(y,530,30):
        obj.rect(i,j,b,b)
  for k in range(300,500):
    obj.rect(i,j,b,b,stroke=1,fill=1)
        
def draw_text(obj,luffy):
  global x1,y1
  for x in naruto:
    for y in x:
      print(y)
      text_obj(luffy,obj,x1,y1,y)
      x1=x1+30
      
    x1=190
    
    y1=y1+30
    
    print(text_obj(luffy,obj,x1,y1,y))

def text_obj(luffy,obj,x1,y1,y):
  luffy.setTextOrigin(x1,y1)
  luffy.setFont("Helvetica-Oblique",12)
  luffy.textLine(text=y)
  obj.drawText(luffy)
  
        
    
if __name__=='__main__':
    obj=canvas.Canvas("boxkullaword9.pdf",pagesize=letter,bottomup=0)
    luffy=obj.beginText()
    draw_border(obj)
    draw_box(obj)
    draw_text(obj,luffy)
    obj.save()
