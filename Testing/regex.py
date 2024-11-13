import re

s = re.compile(r'^\w+\d$')

mo = s.search('aphari75')

print(mo.group())
