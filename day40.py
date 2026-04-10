'''
def find_non_repeating(arr):
    n = len(arr)

    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1

        if count == 1:
            print(arr[i])

# Driver code
arr = [10, 20, 30, 40, 10, 20, 50, 10]
find_non_repeating(arr)
'''
def count(arr, n):
    mp = {}

    for i in range(n):
        if arr[i] in mp:
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1

    for x in mp:
        if mp[x] == 1:
            print(x)    
arr = [10, 30, 40, 20, 10, 20, 50, 10]
count(arr, len(arr))