import re

a= re.compile(r'\w\w\w\w\w\w\d\d\w\w\w\w\w\w\w\w\w\w')
print(a)

mo1=a.search('My mail id :aphari75@gmail.com')
print(mo1)
mo1.group()
#print(mo1.group())
