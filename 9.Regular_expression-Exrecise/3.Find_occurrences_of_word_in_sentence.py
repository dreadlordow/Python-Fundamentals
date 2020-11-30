import re

text = input()
searched = input()
pattern = rf'\b{searched}\b'
matches = re.findall(pattern,text, re.IGNORECASE)

print(f'{len(matches)}')