# find the second smallest element in the array
'''
array = [10, 89, 9, 56, 80, 8]
array.sort()
print(array[1])
'''


import math
array = [10, 89, 9, 56, 80, 8]
first = math.inf
second = math.inf
for i in range(0,len(array)):
    if array[i]<first:
        first=array[i]
for i in range(0, len(array)):
    if array[i] != first and array[i] < second:
        second = array[i]
print("second smallest element is ", second)    
 