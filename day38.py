def count(arr, n):

   
    visited = [False for i in range(n)]
    count_dis=0

  
    for i in range(n):
     
        if (visited[i] == True):
          continue

     
        for j in range(i + 1, n, 1):
            if (arr[i] == arr[j]):
                visited[j] = True
         
        count_dis = count_dis+1;
   
    print(count_dis)


arr = input("Enter the elements of the array separated by space: ").split()
n = len(arr)
count(arr, n)