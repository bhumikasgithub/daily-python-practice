 # find number of integers which has exactly x divisors
num = int(input("Enter a number: "))
divisor=int(input("Enter the number of divisors: "))
count=0
for i in range(1,num+1):
    count_factors = 0
    for j in range(1,i+1):
        if i%j==0:
            count_factors += 1
        else :
            pass
        
    if count_factors == divisor:
        count += 1
print(count)
