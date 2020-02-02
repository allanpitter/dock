#Criando um pdf - utilizando o módulo reportlab
#caso não esteja instalado: pip install reportlab
from reportlab.pdfgen import canvas
c = canvas.Canvas("hello.pdf")
c.drawString(100,100,"Ola Mundo")
c.save()
