from reportlab.lib import utils
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Image, SimpleDocTemplate
def scaled_image(desired_width):
    doc = SimpleDocTemplate("image_with_scaling.pdf", pagesize=letter)
    story = []
    img = utils.ImageReader('Joker.jpg')
    print(img)
    img_width, img_height = img.getSize()#(564,612)
    aspect = img_height / float(img_width)
    print(img_width, img_height)
    img = Image("Joker.jpg",width=desired_width,height=(desired_width * aspect))
    img.hAlign = 'CENTER'
    story.append(img)
    doc.build(story)
if __name__ == '__main__':
    scaled_image(150)
    print("PDF Generated")
