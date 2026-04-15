#python program to find the symmentric pair of the array

def pairofarray(pair):
    s=set()
    for (x,y) in pair:
        s.add((x,y))
        if(y,x) in s:
            print("symmentric pair is ",(y,x))
pair=[(1,2),(3,4),(5,6),(2,1),(7,8)]
pairofarray(pair)   

