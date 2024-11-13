class Students:
    def __init__(self,f_name,l_name,reg_no,email):
        self.f_name=f_name
        self.l_name=l_name
        self.reg_no=reg_no
        self.email=email

    def display(self):
        return self.f_name,self.l_name, self.reg_no,self.email

s1=Students("hari","Ashok",8100025,"aphari75@gmail.com")
print(s1.display())
