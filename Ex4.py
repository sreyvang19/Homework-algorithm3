# EX4.Create function to find Min number in array [2,3,5,0,11,5,2]
def min(array):
    min = 0
    for i in array:
        if i < min:
            min = i
    return min
print(min([2, 3, 5, 0, 11, 5, 2]))