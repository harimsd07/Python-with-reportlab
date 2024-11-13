from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def words(obj,word_list):
    k=0
    for a in range(20):
        x=30
        y=750
        for i in range(0,20):
            
            obj.drawString(x,y,word_list[i])
            y-=36
        x=250
        y=750
        for i in range(20,40):
            obj.drawString(x,y, word_list[i])
            y-=36
        x=500
        y=750
        for i in range(40,50):
            obj.drawString(x,y,word_list[i])
            y-=36
        x=10
        y=750
        for j in range(k+1,k+21,1):
            obj.drawString(x,y,str(j)+".")
            y-=36
        x=210
        y=750
        for j in range(k+21,k+41,1):
           obj.drawString(x,y,str(j)+".")
           y-=36
        x=470
        y=750
        for j in range(k+41,k+51):
          obj.drawString(x,y,str(j)+".")
          y-=36
       
        obj.showPage()
        k=j
                
        


    
   
if __name__=='__main__':
    obj=canvas.Canvas("words 81.pdf",pagesize=letter,bottomup=1)
    word_list = [    " apple",    " banana",    "cherry",    " durian",    " elderberry",    " fig",    " grape",    " honeydew",    " kiwi",    " lemon",    " mango",    " nectarine",    " orange",    " peach",    " quince",    " raspberry",    " strawberry",    " tangerine",    " ugli fruit",    " vanilla bean", " watermelon",    " xigua (Chinese watermelon)",    " yellow watermelon",    " zucchini",    " apricot",    " blackberry",    " cantaloupe",    " dragonfruit",    " elderflower",    " fennel",    " grapefruit",    " honeycrisp apple",    " ice plant",    " jicama",    " kumquat",    " lime",    " lychee",    " mandarin orange",    " nashi pear",    " olive",    " papaya",    " pomegranate",    " quince",    " redcurrant",    " starfruit",    " tangelo",    " ugli fruit",    " vanilla orchid",    " watercress",    " zinfandel grape"]

    print(len(word_list))
    
    words(obj,word_list)
    print("pdf genrated")
    obj.save()
