class Student:
    def __init__(self,name,age,dept):
        self.name = name
        self.age = age
        self.dept = dept

    def display_data(self):
        data ={'name' : self.name,'age': self.age,'dept': self.dept}
        return data

s1=Student('hari','20','CSE')
s2 = Student('jillu','19','medicine')
print(s1.display_data())
print(s2.display_data())
