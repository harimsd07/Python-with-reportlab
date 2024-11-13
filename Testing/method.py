class Irah:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def add(self):
        return (self.a+self.b)
    
    def sub(self):
       return (self.a-self.b)
    
sum = Irah(7,5)
print(sum.add())
print(sum.sub())

