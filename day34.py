# sort the aarray without using sort function
'''
aray = [5, 4, 6, 2, 1, 3, 8, -1]
n=len(aray)
for i in range(0,n):
    for j in range(i+1,n):
        if aray[i]>aray[j]:
            temp=aray[i]
            aray[i]=aray[j]
            aray[j]=temp
print(aray) 
'''      

array = [5, 4, 6, 2, 1, 3, 8, -1]
array.sort(reverse=True)
print(array)