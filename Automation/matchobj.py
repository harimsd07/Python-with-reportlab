import re
pattern= re.compile(r"[a-z,0-9,!,@,#,$,%,&,*,(,),_,+]+@+[a-z]+\.+[a-z]+")
a=pattern.findall(" aphari75@gmail.com and panjuashok1970@gmail.com and some other id's are gk123@gmail.com,abcd@#%66@gmail.com" )
print(a)

