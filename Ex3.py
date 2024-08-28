# EX3.Create function to find Max number in array [2,3,5,0,11,5,2]
def max(array):
    max = 0 
    for i in array:
        if i > max:
            max = i
    return max
print(max([2, 3, 5, 0, 11, 5, 2]))