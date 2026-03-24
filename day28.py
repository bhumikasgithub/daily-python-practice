#python program to find the smallest element from the array
#1
a=[10, 89, 9, 56, 4, 80, 8]
print(min(a))

#2

a=input("Enter the array elements separated by space: ").split()
sorted_a = sorted(a)
print(sorted_a[0])

#3
a = [10, 89, 9, 56, 80, 8]
min_element = a[0]
for i in range (len(a)):
    if a[i]< min_element:
        min_element = a[i]
print(min_element)