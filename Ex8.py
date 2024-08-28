# EX8.Create function to sum total of price 
# products = [
#     {"name": "Apple", "price": 20},
#     {"name": "Orange", "price": 24},
# ]
def sum(product):
    sum = 0
    for i in range(len(product)):
        sum += (product[i]["price"])
    return sum
print(sum([
  {"name": "Apple", "price": 20},
  {"name": "Orange", "price": 24},
]))