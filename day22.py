# find the factorial of the number using resursion 

def getfact(n):
    if n==0:
        return 1
    return n*getfact(n-1)
n=int(input("Enter the number: "))
print (getfact(n))