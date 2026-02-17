# calculate the number of digits in an integer
num=int(input("Enter a number:"))
str_num=str(num)
print("The number of digits in the number is:",len(str_num))


#using while loop 

def count_digits(num):
    count=0
    while num>0:
        num=num//10
        count= count+1
    return count
num=int(input("Enter a number:"))
print(count_digits(num))


#using formula
import math
num=int(input("Enter a number:"))
print(math.floor(math.log10(num)+1))