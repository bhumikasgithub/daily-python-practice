#python program to find the maximum sum of the contigous subarray

def maxsumofarray(arr,n):
    result=arr[0]
    for i in range(n):
        mul=arr[i]
        for j in range(i+1,n):
            mul*=arr[j]
            result= max(result,mul)

        result=max(result,mul)
    return result
arr = [ 1, -2, -3, 0, 7, -8, -2 ]
n = len(arr)
print("Maximum sub-array product is" , maxsumofarray(arr, n))