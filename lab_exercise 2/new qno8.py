
command=""
started=False
# while command !=true
while True:
    command =input(">>>").lower()
    if command=="start":
        if started:
            print("car has already started.")
        else:
            started=True
            print("car has started...!")
    elif command=="stop":
        if not started:
            print("the car has already  stopped")
        else:
            started=False
            print("car has stopped")
    elif command=="help":
        print('''
        start- to start the car 
        stop- to stop the car
        quit - to exit the car
        ''')
    elif command=="quit":
        break
    else:
        print("i donot understand that")







