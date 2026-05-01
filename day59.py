# pyhton program tpo see the parantehese are same or not 

'''
def issame(s):
    c=0
    ans=False
    for i in s:
        if i == '(':
            c+=1
        elif i == ')':
            c-=1
    if c == 0:
        ans=True
    return ans
s="(((()))"
print(issame(s))'''

#2 Second method

def isbalanced(s):
    while True:
        old_s = s   # store previous string
        
        s = s.replace('()', '')
        s = s.replace('[]', '')
        s = s.replace('{}', '')
        
        # if no changes happen, stop loop
        if s == old_s:
            break
    
    # check if all brackets removed
    if len(s) == 0:
        return True
    else:
        return False


# main program
s = input("Enter a string of brackets: ")
print("Given string is balanced:", isbalanced(s))