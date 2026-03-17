# find the factorial of the number using resursion 
'''
def getfact(n):
    if n==0:
        return 1
    return n*getfact(n-1)
n=int(input("Enter the number: "))
print (getfact(n))
'''

def getfact(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

n = int(input("Enter the number: "))
print(getfact(n))