'''#find the lenght of the string using recursion
def string_Len(string):
    if string =="":
        return 0
    else:
        return 1 + string_Len(string[1:])
string = input("Enter a string: ")
print(string_Len(string))'''

def length_str(str):
    i=0
    while str !="":
        i+=1
        str = str[1:]
    return i
string=input("enter a string:")
print ("the lenght of the string is:",length_str(string))