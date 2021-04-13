'''
check whether the given year is leap year or not.if year is leap print'LEAP YEAR'else print'COMMAN YEAR'
hint-a year is a leap year if its number is exactly divisible by 4 and isnot exactly divisible by 100
    -a year is always a leap year if its number is exactly divisible by 400
'''
input_year=int(input("enter year number you Wish"))
if (input_year%400==0) or (input_year%4==0) and (input_year%100!=0):
    print("the year is leap year")
else:
    print("the year isnot a leap year")