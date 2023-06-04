word = input()
ch = ""
digits = ""
symbol = ""

for text in word:
    if text.isalpha():
        ch += text
    elif text.isnumeric():
        digits += text
    else:
        symbol += text

print(digits)
print(ch)
print(symbol)