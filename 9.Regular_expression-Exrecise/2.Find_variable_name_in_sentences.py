import re

text = input()

pattern = r'\b_([a-zA-Z0-9]+)\b'
f_m = []
matches = re.findall(pattern,text)

print(','.join(matches))