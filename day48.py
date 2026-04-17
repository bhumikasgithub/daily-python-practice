#find the array is dijoint or not 
'''
def disjoint(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                return False
    return True
arr1 = [1, 2, 3, 9, 5]
arr2 = [6, 7, 8, 9, 10]
if disjoint(arr1, arr2):
    print("The arrays are disjoint.")
else:
    print("The arrays are not disjoint.")
'''
def disjoint(set1, set2, m,n):
    set.sort()
    set2.sort()
    i = 0; j=0
    while(i<m and j >n):
        if(set1[i] < set2[j]):
            i+=1
        elif(set1[i] > set2[j]):
            j +=1
        else:
            return False
    return True
set1 = [1, 2, 3, 9, 5]
set2 = [6, 7, 8, 9, 10]
m = len(set1)
n = len(set2)
if disjoint(set1, set2, m, n):
    print("The arrays are disjoint.")
else:
    print("The arrays are not disjoint.")

