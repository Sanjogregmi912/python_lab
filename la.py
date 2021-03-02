#for area of rectangle
lenght=float(input("enter the value of lenght of the rectangle:"))
breadth=float(input("enter the value of breath of the rectangle:"))
area=lenght*breadth
print(f"the area of rectangle:{area}")
# for area of triangle
lenght=float(input("Enter the value of lenght:"))
height=float(input("Enter the value of height:"))
area=(lenght*height)/2
print(f"the area of triangle is : {area}")
# for area of circle
radius=float(input("Enter the value of radius:"))
pi=22/7
area = pi*(radius**2)
print(f"The area of circle:{area}")
#pratise
d=input("how far did you travel today (in miles)?")
t=input("how long did it take you(in hours)?")
s=d/t
print("your speed was"+ s +"miles per hours")