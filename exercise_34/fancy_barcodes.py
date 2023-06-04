import re

codes = int(input())
pattern = re.compile(r"@[#]+(?P<found_text>[A-Z][a-zA-Z0-9]{4,}[A-Z])@[#]+")
digit_regex = re.compile(r"\d")

for _ in range(codes):
    barcode = input()
    if pattern.match(barcode):
        digits = digit_regex.findall(barcode)
        product_group = "".join(digits) if digits else  "00"
        print(f"Product code: {product_group}")
    else:
        print("Invalid barcode:")