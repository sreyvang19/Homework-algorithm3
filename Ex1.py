# EX1.Create function to sum numbers in array [1,2,3,4,5,6]
def sum(array):
    sum = 0
    for i in array:
        sum += i
    return sum
print(sum([1, 2, 3, 4, 5, 6]))