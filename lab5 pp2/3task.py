import re

pattern = re.compile(r"[a-z]+_[a-z]+")
print(pattern.findall("khadizha_ishappy_NOT"))