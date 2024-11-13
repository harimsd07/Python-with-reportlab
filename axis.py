from reportlab.graphics import renderPDF,shapes
from reportlab.graphics.charts.axes import XCategoryAxis,YValueAxis

def axis():
    draw=shapes.Drawing(width=500,height=500)
    data = [(5, 10, 15, 20),
        (10, 17, 25, 31)]

    x_axis=XCategoryAxis()
        
    x_axis.setPosition(100, 100, 350)
    x_axis.configure(data, barWidth=None)
    x_axis.categoryNames = ['Python', 'Ruby', 'C++', 'Haskell']
    x_axis.labels.boxAnchor = 'n'
    x_axis.labels[0].angle = 45
    x_axis.labels[0].fontName = 'Times-Bold'
    x_axis.labels[1].fontName = 'Courier'
    x_axis.labels[1].fontSize = 16
    draw.add(x_axis)


    y_axis = YValueAxis()
    y_axis.setPosition(100, 100, 150)
    y_axis.configure(data)
    draw.add(y_axis)
    renderPDF.drawToFile(draw, 'axes_demo.pdf')

if __name__=="__main__":
    axis()
print("PDF Generated")
