import re
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<!@#$%^&*(+)+++> for dinner.>')
print( mo.group())

