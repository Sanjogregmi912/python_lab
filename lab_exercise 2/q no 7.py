'''
game finding a secret number within 3 attempts using while loop
'''
num=0
secret_num=6
while num<=2:
    num+=1
    num1=num
    guess=int(input("enter any number"))
    
    if guess==secret_num:
        print("your guess is right")
    else:
        print("your guess isnot right,try again!!")