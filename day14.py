# program to find the largest element in the array

def findmax(a,n):
    if n==1:
        return a[0]
    return max(a[n-1],findmax(a,n-1))
if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    n = len(a)
    print("The largest element is", findmax(a, n))