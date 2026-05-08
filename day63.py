# python program to find theleng of the string without usiing len() function 

str = input("Enter the string: ")
length = 0
for i in str:
    length += 1
print(length)