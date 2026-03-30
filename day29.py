# find max and min element from the array

'''array = [10, 89, 9, 56, 4, 80, 8]
minelement = array[0]
maxelement = array[0]
for i in range (len(array)):
    if array[i] < minelement:
        minelement = array[i]
    if maxelement < array[i]:
        maxelement = array[i]
print("Minimum ", minelement, "Maximum ", maxelement, sep="\n")
'''
#2

array = [10, 89, 9, 56, 80, 8]
array.sort()
print("minelement",array[0], "maxelement", array[-1], sep="\n")




