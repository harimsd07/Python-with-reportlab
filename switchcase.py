
n=int(input())
m=int(input())

def add():
    return n+m

def subs():
    return n-m

def prod():
    return n*m

def div():
    return m/n

def rem():
    return m%n

def operations(op):
    switch={'+': add(),'-': subs(),'*': prod(),'/': div(),'%': rem()}
    return switch.get(op,'Choose one of the following operator:+,-,*,/,%')

print(operations("*"))

operations('^')
