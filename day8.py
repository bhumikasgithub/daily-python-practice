#check the number of days in the month of that year

month=int(input("Enter the month number:"))
year=int(input("Enter the year:"))
if((month==2) and ((year%4==0)  or ((year%100==0) and (year%400==0)))) :
    print("Number of days is 29")
elif(month==2):
    print("Number of days is 28")
elif(month in [1,3,5,7,8,10,12]):
    print("Number of days is 31")
else:
    print("Number of days is 30")