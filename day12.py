#Power of a Number using Recursion in Python
def power(a,b):
   if b!=0:
    return a*power(a,b-1)
   else:
     return 1
a=float(input("Enter a: "))
b=int(input("Enter b: "))
print(power(a,b))