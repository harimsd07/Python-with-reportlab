class Student:
    def __init__(Irah,reg_no,pg):
        Irah.name=[1,2,3,4,5,6,7,8,0]
        Irah.reg_no=reg_no
        Irah.phone_num=pg
    def display(Irah):
        print("Name :",Irah.name)
        print("Reg :",Irah.reg_no)
        print("Phone no:",Irah.phone_num)
        for i in Irah.name:
            print(i)
    
    
    
y= input()
z= input()
stud=Student(y,z)
stud.display()

#print(stud.name,stud.reg_no,stud.pg)
stud.phone_num()

#stud.display("hari",25)
#print(stud.Phone_num)
  

