import re

input = "Codes: 121, 12321, 45654, 789, 123456"
s = re.findall(r"\b\d{3,6}\b", input)
palin = [num for num in s if num == num[::-1]]

print(palin)
