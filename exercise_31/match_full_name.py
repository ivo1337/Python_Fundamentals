import re
name = input()
pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
results = re.findall(pattern, name)

print(*results)