#find the sum of the elements in the array
'''
array = [10, 89, 9, 56, 80, 8]
sum = 0 
for i in range(0 , len(array)):
    sum += array[i]
print(sum)



array = [10, 89, 9, 56, 80, 8]
print(sum(array))
'''

def sum_array(array, n):
    if n==0:
        return 0
    return array[n-1]+sum_array(array, n-1)
array= [10, 89, 9, 56, 80]
print(sum_array(array, len(array)))
