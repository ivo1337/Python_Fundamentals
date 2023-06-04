product = input()
quantity_of_the_product = int(input())

product_info = {
    "coffee": 1.50,
    "coke": 1.40,
    "water": 1.00,
    "snacks": 2.00
}

def calculate(product_type, how_many):
    result = product_info[product_type] * how_many
    return f"{result:.2f}"
print(calculate(product, quantity_of_the_product))
