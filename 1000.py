from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def words(obj,word_list):
    x=30
    y=30
    for i in range(1,21,1):
        obj.drawString(x,y,str(i)+word_list[i])
        y+=40
    x+=200
    y=30
    for i in range(21,41,1):
        obj.drawString(x,y,str(i)+word_list[i])
        y+=40
    x+=200
    y=30
    for i in range(41,51,1):
        obj.drawString(x,y,str(i)+word_list[i])
        y+=40
    obj.showPage()

def word(obj,word_list):
    x=30
    y=30
    for i in range(51,71,1):
        obj.drawString(x,y,str(i)+word_list[i-51])
        y+=40
    x+=200
    y=30
    for i in range(71,91,1):
        obj.drawString(x,y,str(i)+word_list[i-71])
        y+=40
    x+=200
    y=30
    for i in range(91,101,1):
        obj.drawString(x,y,str(i)+word_list[i-91])
        y+=40
    obj.showPage()
    
def jolly(obj,word_list):
    x=30
    y=30
    for i in range(101,121,1):
        obj.drawString(x,y,str(i)+word_list[i-101])
        y+=40
    x+=200
    y=30
    for i in range(121,141,1):
        obj.drawString(x,y,str(i)+word_list[i-121])
        y+=40
    x+=200
    y=30
    for i in range(141,151,1):
        obj.drawString(x,y,str(i)+word_list[i-141])
        y+=40
    obj.showPage()
    
def word200(obj,word_list):
    x=30
    y=30
    for i in range(151,171,1):
        obj.drawString(x,y,str(i)+word_list[i-151])
        y+=40
    x+=200
    y=30
    for i in range(171,191,1):
        obj.drawString(x,y,str(i)+word_list[i-171])
        y+=40
    x+=200
    y=30
    for i in range(191,201,1):
        obj.drawString(x,y,str(i)+word_list[i-191])
        y+=40
    obj.showPage()
    
def word300(obj,word_list):
    x=30
    y=30
    for i in range(201,221,1):
        obj.drawString(x,y,str(i)+word_list[i-201])
        y+=40
    x+=200
    y=30
    for i in range(221,241,1):
        obj.drawString(x,y,str(i)+word_list[i-221])
        y+=40
    x+=200
    y=30
    for i in range(241,251,1):
        obj.drawString(x,y,str(i)+word_list[i-241])
        y+=40
    obj.showPage()
    
def word400(obj,word_list):
    x=30
    y=30
    for i in range(251,271,1):
        obj.drawString(x,y,str(i)+word_list[i-251])
        y+=40
    x+=200
    y=30
    for i in range(271,291,1):
        obj.drawString(x,y,str(i)+word_list[i-271])
        y+=40
    x+=200
    y=30
    for i in range(291,301,1):
        obj.drawString(x,y,str(i)+word_list[i-291])
        y+=40
    obj.showPage()
    
def word500(obj,word_list):
    x=30
    y=30
    for i in range(301,321,1):
        obj.drawString(x,y,str(i)+word_list[i-301])
        y+=40
    x+=200
    y=30
    for i in range(321,341,1):
        obj.drawString(x,y,str(i)+word_list[i-321])
        y+=40
    x+=200
    y=30
    for i in range(341,351,1):
        obj.drawString(x,y,str(i)+word_list[i-341])
        y+=40
    obj.showPage()
    
def word600(obj,word_list):
    x=30
    y=30
    for i in range(351,371,1):
        obj.drawString(x,y,str(i)+word_list[i-351])
        y+=40
    x+=200
    y=30
    for i in range(371,391,1):
        obj.drawString(x,y,str(i)+word_list[i-371])
        y+=40
    x+=200
    y=30
    for i in range(391,401,1):
        obj.drawString(x,y,str(i)+word_list[i-391])
        y+=40
    obj.showPage()
    
def word700(obj,word_list):
    x=30
    y=30
    for i in range(401,421,1):
        obj.drawString(x,y,str(i)+word_list[i-401])
        y+=40
    x+=200
    y=30
    for i in range(421,441,1):
        obj.drawString(x,y,str(i)+word_list[i-421])
        y+=40
    x+=200
    y=30
    for i in range(441,451,1):
        obj.drawString(x,y,str(i)+word_list[i-441])
        y+=40
    obj.showPage()
    
if __name__=='__main__':
    obj=canvas.Canvas("1000_words21.pdf",pagesize=letter,bottomup=0)
    word_list = [" apple","badboy"," banana",    "cherry",    " durian",    " elderberry",    " fig",    " grape",    " honeydew",    " kiwi",    " lemon",    " mango",    " nectarine",    " orange",    " peach",    " quince",    " raspberry",    " strawberry",    " tangerine",    " ugli fruit",    " vanilla bean", " watermelon",    " xigua (Chinese watermelon)",    " yellow watermelon",    " zucchini",    " apricot",    " blackberry",    " cantaloupe",    " dragonfruit",    " elderflower",    " fennel",    " grapefruit",    " honeycrisp apple",    " ice plant",    " jicama",    " kumquat",    " lime",    " lychee",    " mandarin orange",    " nashi pear",    " olive",    " papaya",    " pomegranate",    " quince",    " redcurrant",    " starfruit",    " tangelo",    " ugli fruit",    " vanilla orchid",    " watercress",    " zinfandel grape"]
    words(obj,word_list)
    word(obj,word_list)
    jolly(obj,word_list)
    word200(obj,word_list)
    word300(obj,word_list)
    word400(obj,word_list)
    word500(obj,word_list)
    word600(obj,word_list)
    word700(obj,word_list)
    print("pdf genrated")
    obj.save()
