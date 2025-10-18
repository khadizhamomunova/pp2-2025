import re
inputtext = "Valid {one}, {two123}, invalid {nested {bad}}"
match = re.findall(r"\{[^{}]*\}", inputtext)
print(match)  
