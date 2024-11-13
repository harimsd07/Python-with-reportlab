from reportlab.platypus import Flowable

class RectBorder(Flowable):
    def __init__(self,x=30,y=30,width=430,height=620):
        Flowable.__init__(self)
        self.x=x
        self.y=y
        self.width=width
        self.height=height

    def aBorder(self):
        print("k")

obj = RectBorder()
obj.aBorder()
