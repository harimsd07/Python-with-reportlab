from reportlab.lib import colors
from reportlab.graphics import shapes,renderPDF

def draw_shapes():
    draw=shapes.Drawing(300,300)#(x,y) here x and y are height and width of the working area/the area were the shapesnget placed.
    draw.add(shapes.Circle(150,150,50,fillColor=colors.red))#(x,y,radius) x and y are the coordinates.
    renderPDF.drawToFile(draw,"shapes.pdf",msg="The Circle")

if __name__=="__main__":
    draw_shapes()
print("PDF Generated")
