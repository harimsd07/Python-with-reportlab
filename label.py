from reportlab.lib import colors
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import shapes,renderPDF

def fun():
    draw=shapes.Drawing(300,300)
    draw.add(shapes.Rect(200,50,50,50,fillColor=colors.red))

    x=50
    angle=0
    for i in range(3):
        label=Label()
        label.setOrigin(200,100)
        label.boxAnchor ="sw"
        label.angle=angle
        label.setText("This is IRAH")
        draw.add(label)

        x+=25
        angle+=45
    renderPDF.drawToFile(draw,"label.pdf",)

if __name__=="__main__":
    fun()
print("PDF Generated")
        
