'''
# find the HCF of two numbers
def hcf(a,b):
    if b==0:
        return a
    return hcf(b,a%b)
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))
print("The HCF of", num1, "and", num2, "is", hcf(num1, num2))
'''
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
print("The HCF of", num1, "and", num2, "is", hcf)