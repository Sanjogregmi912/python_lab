'''
given a three-digit number ,find the sum of its digit
'''
user_input=int(input("enter the three digit number"))
sum=0
while user_input>0:
    reminder=user_input%10
    sum=sum+reminder
    user_input=user_input//10
print("the sum of the given number is",sum)