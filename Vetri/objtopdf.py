from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import PCMYKColor, PCMYKColorSep, Color, black, blue, red

name = ["one", "two", "three"]
num = [1,2,3]
wobjs = []
pos_y =[50]
      
class wtopdf:
    def __init__(self, name, num):
        self.name = name
        self.num = num
    def display(self):
        print(self.name, self.num)



    def font_demo(self, my_canvas):
      pos_x = 50
      my_canvas.setFontSize(15)
      my_canvas.setFillColor(Color(0,0,30))
      my_canvas.drawString(pos_x,pos_y[0],self.name+"  "+str(self.num))
      pos_y[0]+=40
      print(pos_y[0])
      



    
if __name__=='__main__':
  my_canvas=canvas.Canvas("van.pdf",pagesize=letter,bottomup=0)
  wo=["wo1", "wo2", "wo3"]
  for i in range(0,3):
      wo[i] = wtopdf(name[i], num[i])
      wobjs.append(wo[i])
      wo[i].display()
      wo[i].font_demo(my_canvas)
  my_canvas.save()
