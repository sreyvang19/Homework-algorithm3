# EX6.Create function to count positive number in array [-1,11,2,0,-1,4]
def count(array):
    count = 0
    for i in array:
        if i >= 0:
            count += 1
    return count
print(count([-1, 11, 2, 0, -1, 4]))