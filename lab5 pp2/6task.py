import re

text = "Hello My name, is. Khadizha, so you can call me by my name"
replacedText = re.sub(r'[ ,.]', ':', text)
print(replacedText)