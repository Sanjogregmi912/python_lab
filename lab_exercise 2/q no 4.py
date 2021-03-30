''' if temperature is greater than 30,
its a hot day otherwise if its less than 10
its a cold day; otherwise
its neither hot nor cold

'''
user_temperature=int(input("enter the temperature of a day:"))
if user_temperature >30:
    print("its a hot day")
elif (user_temperature<10):
    print("its a cold day")
else:
    print("its neither hot nor cold")