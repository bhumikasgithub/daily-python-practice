#1#
num=int(input("Enter the number : "))
val=str(num)
Replace=val.replace('0','1')
print(Replace)

#2#
#taking Input
n=int(input('Enter number: '))
#converting into string
n=str(n) 
#then into the list
n=list(n)
r="" #empty string for addind it the item of list
for i in range(len(n)):
    #if we find '0' we will replace it with '1'
    if(n[i]=='0'):
        n[i]='1'
    r=r + n[i]  #creating the new integer 
del n    
print("Converted number is :",int(r))
