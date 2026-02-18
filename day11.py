# find the root of the equestions
def roots(a,b,c):
    d=b**2-4*a*c
    if d>=0:
        r1 = (-b + d**0.5)/(2*a)
        r2 = (-b - d**0.5)/(2*a)
        print(r1,r2)
    else:
        print("No real roots")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

roots(a, b, c)