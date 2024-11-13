from reportlab.pdfgen.canvas import Canvas

canvas = Canvas("example.pdf")
canvas.setFont("Helvetica", 10)
canvas.drawString(100, 100, "This is a line of text.")
canvas.drawString(100, 120, "This is another line of text with custom leading.")
canvas.set_leading(12)
canvas.drawString(100, 140, "This line has a leading of 12 points.")
canvas.showPage()
canvas.save()
