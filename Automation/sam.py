import re

a= re.compile(r"2/162,kannimar kovil street, trichy-620014")
b=a.search("\d\W\d\d\d")
print("text found:"+b.group())

