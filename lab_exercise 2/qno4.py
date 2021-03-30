''' if name is less than 3 character long-name must be at least 3 characters
otherwise if it's more than 50 characters- name must be maximum of 50 charcters
otherwise - name looks good

'''
user_name=input("enter your good name")
lenght_username=len(user_name)
if (lenght_username<=3):
    print("your name is not valid")
elif (lenght_username>=50):
    print("it also cannot be valid")
elif (lenght_username>3) and (lenght_username<50):
    print("your name is valid")