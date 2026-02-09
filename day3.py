num = int(input("Enter the number: "))

# function to check prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

found = False

# check pairs
for i in range(2, num):
    if is_prime(i) and is_prime(num - i):
        print(i, "and", num - i, "are prime numbers whose sum is", num)
        found = True
        break

if not found:
    print("No prime numbers can give sum of", num)
