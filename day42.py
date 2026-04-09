# vector producrt of 2 arrays

arr1 = [1, 2, 6, 3, 7]
arr2 = [10, 7, 45, 3, 7]

n = len(arr1)

#Sort arr1 in ascending order
for i in range(n):
    for j in range(i+1, n): 
        if arr1[i]>arr1[j] :
            arr1[i], arr1[j] = arr1[j], arr1[i]

#Sort arr2 in descending order
for i in range(n):
    for j in range(i+1, n): 
        if arr2[i]<arr2[j] :
            arr2[i], arr2[j] = arr2[j], arr2[i]

product = 0
for i in range(n):
    product += arr1[i]*arr2[i]

print(product)
'''
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
arr1.sort()
arr2.sort(reverse=True)
producrt = 0
n=len(arr1)
for i in range(n):
    producrt += arr1[i] * arr2[i]
print(producrt)
'''


