'''
given three integres ,print the smaller one(three integers should be user input)

'''
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num3=int(input("enter the third number:"))
if num1<num2 and num1<num3:
    print(f"the first input is smaller:{num1}")
elif num2<num1 and num2<num3:
    print(f"the second input is smaller:{num2}")
else:
    print(f"the third number is smaller:{num3}")