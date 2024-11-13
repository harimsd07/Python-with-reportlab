class Entertaiment_1:
    def __init(self,name,episode):
        self.name=name
        self.episode=episode
        
    def webseries(self,name,episodes):
        print(self.name,self.episodes,sep="\n")

class Entertaiment_2(Entertaiment_1):
    def __init(self,name,episode):
        Entertaiment_1.__init(self,name,episode)
        print(self.name,self.episodes,sep="\n")

c=Entertaiment_2("Dark",26)
c.webseries()

        
