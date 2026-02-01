import calendar
year = int(input("enter year :"))
print(calendar.calendar(year))
 
#single month calender 
import calendar
year = int(input("Enter year"))
month = int(input("Enter month (1-12):"))
print(calendar.month(year,month))
#Check leap year 
import calendar
year = int(input("Enter year:"))
if calendar.isleap(year):
    print("Leap year")                                                                       
else:
    print("Not leap year")
    #simple logic\
    year = int(input("enter year:"))
    month = int(input("enter month(1-12):"))
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    # leap year check 
    if (year % 4 == 0 and year % 100 != 0) or(year % 400 == 0 ):
        days[1] = 29
        print("Total days:",days[month-1])

