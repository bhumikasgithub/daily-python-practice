'''# finde the  smallest element of thd array 
def smallest(a,n):
    if n==1:
        return a[0]
    return min(a[n-1],smallest(a,n-1))
if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    n = len(a)
    print("The smallest element is", smallest(a, n))'''

aray = [1, 2, 3, 4, 5]
sorted_array = sorted(aray)
minimum = min(sorted_array)
print("The smallest element is", minimum)