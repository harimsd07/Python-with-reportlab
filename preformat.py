from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Preformatted,SimpleDocTemplate
from reportlab.lib.pagesizes import letter

doc=SimpleDocTemplate("maxlinelenght.pdf",pagesize=letter)
styles = getSampleStyleSheet()
code_style = styles["Code"]

mtlist=[]                    

text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut odio ac dui porttitor rhoncus. Vestibulum feugiat lectus et mauris tristique, in laoreet lectus lobortis. Proin lacinia dui a nisl auctor, sit amet tempus nunc viverra. Curabitur vitae scelerisque dui. Integer commodo blandit nulla, eu fermentum mi hendrerit in. Nullam vitae risus et libero fermentum cursus. Aenean aliquam lorem non dui ultrices, eu euismod elit tincidunt. Maecenas vel nunc bibendum, pellentesque felis in, pellentesque nunc. Nam mattis ante eget orci gravida sollicitudin. Cras iaculis sem sit amet justo laoreet elementum. Donec at posuere enim, et fermentum mauris. Ut laoreet dolor at interdum efficitur.
"""

preformatted = Preformatted(text, style=code_style, maxLineLength=80)
mtlist.append(preformatted)
doc.build(mtlist)
# Render the preformatted text to a PDF document

