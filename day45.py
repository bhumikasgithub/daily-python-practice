# python program to find the odd and even number in the array
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n=len(arr)
for i in range(n):
    if arr[i]%2==0:
       print(arr[i],"even")
    else :
       print(arr[i],"odd")

arr= [1, 2, 3, 4, 5, 6, 7, 8, 9]
n=len(arr)
countodd = 0
counteven = 0
for i in range(0,n):
    if arr[i]%2==0:
        counteven += 1
    else:
        countodd +=1
print("number of even number is ",counteven)
print("number of odd number is ",countodd)


arr = [1, 7, 8, 4, 5, 16, 8]
n = len(arr)
countEven = 0
countodd = 0
for i in range(0, n):
    if arr[i]&1==0 :
        countEven += 1
    else:
        countodd += 1

print("Even Elements count : " )
print(countEven)

print("Odd Elements count : ")
print(countodd)