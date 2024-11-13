class Prime:
    def __init__(irah,num):
        irah.num = num
        if(num>1):
            for i in range(2,num):
                if(num%i)==0:
                    flag = True
                    break
        if(flag):
            print("Not prime number")
        else:
            print("prime number")
num = int(input())
a = Prime(num)