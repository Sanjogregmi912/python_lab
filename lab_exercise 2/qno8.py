'''
help
start-to start the car
stop-to stop the car
quit-to exit
asd
i donot understand this
start
car started .. ready to go
stop
car stopped
quit

'''
command_repeat=0
first_command="start"
second_command="stop"
third_command="exit"

while command_repeat<=2:
    command_repeat+=1
    user_command = input("enter any command").lower()
    if user_command==first_command:
        print("car started...ready to go!!")

    elif user_command==second_command:
        print("car stopped..")

    elif user_command==third_command:
        break
    else:
        print("i donot understand this")

