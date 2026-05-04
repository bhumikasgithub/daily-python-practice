#calculate is alphabet or not in the python


ch = input("enter the charecture: ")

if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
    print("it is alphabet")
else:    
    print("it is not alphabet")    



if 96 < ord(ch) < 123 or 64 < ord(ch) < 91:
    print("it is alphabet")
else:
    print("it is not alphabet")
