class Number:
    def __init__(irah,num):
        irah.num = num
        if (irah.num % 2== 0):
            print("even")
           
        else:
            print("odd")

num = int(input())
a=Number(num)
            