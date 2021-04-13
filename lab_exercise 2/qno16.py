'''
write a python program to sum of three given number .however if two value are equal sum will be zero.
'''
def sum(x,y,z):
    if x==y or y==z or z==x:

        print("sum is zero")
    else:
        print(f"the sum is:{x+y+z}")


x=int(input("enter the first number"))
y=int(input("enter the second number"))
z=int(input("enter the third number"))
sum(x,y,z)