#Given the interger n - the number of minute that is passed since midnight-how many hours and minute are displayed on the 24 hours digital clock?
#the program should print two number the number of hours (between 0 and 23 and the number of minute (between 0 and 59)
N=int(input("Enter the minute passed since midnight:"))
hours= (N//60)
minutes= (N%60)
print(f"the hours is {hours}")
print(f"the minutes is{minutes} ")
print(f"Its {hours}:{minutes}now")