'''def countFreq(arr, n):

   visited = [False for i in range(n)]

   for i in range(n):

     if (visited[i] == True):
        continue

     count = 1
     for j in range(i + 1, n, 1):
        if (arr[i] == arr[j]):
          visited[j] = True
          count += 1

     print(arr[i], count)

# Driver Code
arr = [10, 30, 10, 20, 10, 20, 30, 10]
n = len(arr)
countFreq(arr, n)
'''
def countFreq(arr, n):
    map= dict()
    for i in range(n):
        if arr[i] in map.keys():

            map[arr[i]]+=1
        else:
            map[arr[i]]=1
    for x in map:
        print(x, map[x])
arr = [10, 30, 10, 20, 10, 20, 30, 10]
n = len(arr)
print(countFreq(arr, n))