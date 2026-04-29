#python prpgram to impletment the jaggle algorithm in array

import math 
def leftrotate(arr,d,n):
    for i  in range(math.gcd(d,n)):
        temp = arr[i]
        j=i
        while 1:
            k = j + d
            if k >= n:
                k = k-n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
            arr[j] = temp
arr = list(map(int,input("Enter the array elements: ").split()))
n = len(arr)
no_of_rotations = int(input("Enter the number of the rotaations:"))

print("Array before rotation: ")
print(*arr)
leftrotate(arr, no_of_rotations,n)
print("\nArray Elements after left rotation: ")
print(arr)