
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

a=30
t=['cap']
def draw_shape(b):
 
  for i in range(150,450,30):
    for j in range(200,500,30):
      b.rect(i,j,a,a)
  for k in range(i,j):
       b.drawString(i,j,t)
     
      
      
  b.line(30,30,565,30)#upper 
  b.line(30,30,30,805)#left
  b.line(565,30,565,805)#right
  b.line(30,805,565,805)#base   
      
  #a.rect(180,200,30,30,stroke=1,fill=0)

  b.save()
if __name__=='__main__':
  b= canvas.Canvas("box1.pdf",bottomup=0)
  draw_shape(b)
