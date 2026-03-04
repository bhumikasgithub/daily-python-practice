# find the lcm of the numbers using recursion

def hcf(a,b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)
def lcm(a,b):
    return (a * b)//hcf(a,b)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))  
print("The LCM of", num1, "and", num2, "is", lcm(num1, num2))


    