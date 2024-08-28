# EX10.Show product name that has maximum price

# products = [
#     {"name": "Apple", "price": 20},
#     {"name": "Orange", "price": 24},
# ]
def max(product):
    max = 0 
    for i in range(len(product)):
        if i > max:
            max = (product[i]["name"])
    return max
print(max([
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},
]))