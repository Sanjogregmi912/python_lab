"""
weight converter:
input the weight of person in either kg or lbs.
 if the person provides his/her
 weight in kg then convert it into lbs else convert it to kg

"""
user_weight=float(input("please enter your weight:\n"))
user_choice=input("choose if u want to convert it into kg or pounds\n")
if (user_choice=="kg"):
    print(f"the weight in pounds is{user_weight*2.20462262}")
elif(user_choice=="pounds"):
    print(f"the weight in kg is{user_weight* 0.45359237}")
else:
    print("it isnot recongized")
