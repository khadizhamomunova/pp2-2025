import re

input = "Call me at +7-707-123-45-67 or 8(777)321-45-67"
match = re.findall(r'(\+7|\b8)\D?(\d{3})\D?(\d{3})\D?(\d{2})\D?(\d{2})', input)
norm = []
for match in match:
    norm.append("+7" + "".join(match[1:]))

print(norm)
