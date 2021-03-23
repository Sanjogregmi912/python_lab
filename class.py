import random
number=random.randint(1,10)

#first method
#guess=int(input("guess the number"))
#while number !=guess:
    #guess=int(input("oops!!try again:"))
#else:
    #print("congrautlation!! u are right")


 #second method
while True:
    guess= int(input("please guess the number?"))
    if guess==number:
        print("la badai cha")
        break
    else:
        print("oops try again")
