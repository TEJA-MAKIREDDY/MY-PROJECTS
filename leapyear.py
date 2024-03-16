#checking if the year is a leap year or not
#if the year IS divisible by 4 and not by 100 or if it is div by 400 then it is leap year
year =int(input("enter year"))
if (year%4==0 and year%100!=0) or year%400==0:
     print("leap year")
else:
    print("not a leap year")
