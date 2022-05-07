import re

text = "She is a 20-year-old 1.7m \"girl\"."
res = re.findall("[^-\d\"][a-zA-Z]+", text)
# res = re.findall("^(\"\w+)", text)
print(res)
