import re

string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'

result = re.split(pattern, string) 
print(result)

#it start to spilt if number exist according to the given pattern


#spilt method

string = 'Twelve:12 Eighty nine:89 Nine:9.'
pattern = '\d+'

# maxsplit = 1
# split only at the first occurrence
result = re.split(pattern, string, 1) 
print(result)
# IN SPILT method we can also pass the argument,which spilt the given string according to the given value which is known as maxspilt


# Sub method
string = 'abc 12\de 23 \n f45 6'

# matches all whitespace characters
pattern = ' '

# empty string
replace = ""

new_string = re.sub(pattern, replace, string) 
print(new_string)

# Here we can add another parameter in which we can select the renge for the patten to appily in the given string.
