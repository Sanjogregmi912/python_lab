#write a program to take a input from the user, ask the user age.if the user age is below 15 print a message you are a child
# if the user age is greater than 15 and lesser than 40 print a message u are a adult,if user age is greater 40 print a message u are old
age=int(input("Enter your age"))
if age<=15:
    print("u are an infant")
elif age>=15 and age<=40:
    print("u are an adult")
else:
    print("u are old")
