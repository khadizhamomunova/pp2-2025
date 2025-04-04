import re

pattern = re.compile(r'the')
c= str(input())
print(pattern.findall(c))