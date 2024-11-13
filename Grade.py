class MarkList:
    def __init__(irah,sub1,sub2,sub3,sub4,sub5):
        irah.sub1 = sub1
        irah.sub2 = sub2
        irah.sub3 = sub3
        irah.sub4 = sub4
        irah.sub5 = sub5
    def display(irah):
         print("sub1 :",irah.sub1)
         print("sub2 :",irah.sub2)
         print("sub3 :",irah.sub3)
         print("sub4 :",irah.sub4)
         print("sub5 :",irah.sub5)
           
     

a = int(input("tamil"))
b = int(input("english"))
c = int(input("maths"))
d = int(input("science"))
e = int(input("social"))
mark = MarkList(a,b,c,d,e)
mark.display()

total =a+b+c+d+e
print(total)
avg = total/5
print(avg)

if avg>=91 and avg<=100:
    print("Your Grade is A1")
elif avg>=81 and avg<91:
    print("Your Grade is A2")
elif avg>=71 and avg<81:
    print("Your Grade is B1")
elif avg>=61 and avg<71:
    print("Your Grade is B2")
elif avg>=51 and avg<61:
    print("Your Grade is C1")
elif avg>=41 and avg<51:
    print("Your Grade is C2")
elif avg>=33 and avg<41:
    print("Your Grade is D")
elif avg>=21 and avg<33:
    print("Your Grade is E1")
elif avg>=0 and avg<21:
    print("Your Grade is E2")
else:
    print("Invalid Input!")





