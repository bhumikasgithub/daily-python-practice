#python programe to sort thr arry lement according to the second arry
from collections import Counter
def solve(arr1,arr2):
    res=[]
    f = Counter(arr1)
    for e in arr2:
        res.extend([e]*f[e])
        f[e]=0

    rem = list(sorted(filter(lambda x: f[x] > 0, f.keys())))
    for e in rem:
        res.extend([e]*f[e])

    return res
arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]   
print(solve(arr1,arr2))