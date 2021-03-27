Year=int(input("enter the year"))
if Year%4==0 and Year%100!=0 or Year%400==0:
    print(Year,"It is a leap year")
else :
    print(Year,"It is not leap year")