#find the array is dijoint or not 
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

