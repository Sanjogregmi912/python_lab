'''
given a positive number print its fractional part
'''
import math
user_input=float(input("enter any number:"))
fractional_part=math.modf(user_input)
print(fractional_part)