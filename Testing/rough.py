message ='hari bcde jklsm 5'
count={}
for character in message:
    count.setdefault(character,0)
    count[character]=count[character]+1

print(count)

