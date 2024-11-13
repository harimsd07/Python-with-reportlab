while True:
     print('Enter your age:')
     age = input()
     try:
         age = int(age)
     except:
         print('Please use numeric digits.')
         continue
         print(age)

     if age < 1:
         print('Please enter a positive number.')
         continue
     break
print(f'Your age is {age}.')

import 
