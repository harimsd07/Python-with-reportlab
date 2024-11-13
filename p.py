from reportlab.pdfgen import canvas
a=canvas.Canvas("pd.pdf",bottomup=0)
a.rect(40,30,30,30)
a.rect(70,30,30,30)
a.save()
