def leftrotate(arr, d, n):
    if(d == 0 or d == n):
        return
    i = d
    j = n - d
    while(i != j):
        if(i < j):
            swap(arr, d - i, d + j - i, i)
            j -= i
        else:
            swap(arr, d - i, d, j)
            i -= j
    swap(arr, d - i, d, i)


def swap(arr, fi, si, d):   # ✅ fixed indentation
    for i in range(d):
        temp = arr[fi + i]
        arr[fi + i] = arr[si + i]
        arr[si + i] = temp


arr = [1, 2, 3, 4, 5, 6, 7]
leftrotate(arr, 2, 7)

for i in range(7):
    print(arr[i], end=" ")