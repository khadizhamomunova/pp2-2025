import re

text = "MyNameIsKhadizha"

words = re.findall(r'[A-Z][^A-Z]*', text)
print(words)