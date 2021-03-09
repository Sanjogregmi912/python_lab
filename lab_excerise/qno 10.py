#write a python to convert seconds to days, hours, minutes, and seconds.
user_seconds=int(input("enter the seconds you want to convert"))
seconds_into_days=user_seconds/(60*60*24)
seconds_into_hours=user_seconds/(60*60)
seconds_into_minutes=user_seconds/60
seconds_into_seconds=user_seconds
print(f"the number of day in that seconds is{seconds_into_days}\n and into hours is{seconds_into_hours} \nand into minutes is{seconds_into_minutes} \nand seconds is{seconds_into_seconds}")
