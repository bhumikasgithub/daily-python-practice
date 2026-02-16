'''# count the numbe of time th eperticular digit appares in th number
num=int(input("Enter a number:"))
digit=int(input("Enter a digit:"))

count=0
temp=num

for i in range(len(str(num))):
    if temp%10==digit:
        count+=1
    temp//=10

print(count)
'''''

#2
num = input("Enter a number: ")
digit = input("Enter a digit: ")

count = 0

for i in num:
    if i == digit:
        count += 1

print(count)

