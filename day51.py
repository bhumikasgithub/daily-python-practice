#Write a program to find the sum of minimum absolute difference using python
import sys
def min_abs_diff(arr,n):
    result = sys.maxsize
    for i in range(0,n):
        sum = 0;
        for j in range(0,n):
            sum += abs(arr[i]-arr[j])
        result = min(result,sum)
    return result;

arr = [1, 2, 3]
n = len(arr)
print(min_abs_diff(arr,n))

        
