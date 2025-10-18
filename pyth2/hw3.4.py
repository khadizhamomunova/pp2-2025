import re

info = ["0x1A3F", "0XFF", "123ABC", "0xZZZ"]
valid = re.compile(r"^(0x|0X)[0-9A-Fa-f]+$")

result = [bool(valid.match(s)) for s in info]
print(result)
