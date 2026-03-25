#print largest element in the array array from user input

1
array = [int(x) for x in input("Enter the array elements separated by space: ").split()]
print(max(array))

2
def largest(array):
    max_A = array[0]
    for i in range(1, len(array)):
        if array[i]>max_A:
            max_A = array[i]
    return max_A
array = [int(x) for x in input("Enter the array elements separated by space: ").split()]
print(largest(array))
 
3 
a = [10, 89, 9, 56, 4, 80, 8]
a.sort()

print (a[-1])

4
a = [10, 89, 9, 56, 4, 80, 8]
max_element = a[0]

for i in range(len(a)):
  if a[i] > max_element:
     max_element = a[i]

print (max_element)


