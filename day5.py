# calculating the area of the circle

R=float(input("Enter the radius of the circle: "))
Area=3.14*R*R
print(Area)


# prime number code from 1 to 100
for i in range(1, 101):
        for n in range(2,i):
            if(i % n) == 0:
                break
        else:
             print(i,end=" ")

