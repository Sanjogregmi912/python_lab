#write a program reads the lenght of the base and the height of right angled triangle and prints the area . Every number is given on a seprate line
Height=float(input("Enter the  height of the triangle"))
Base=float(input("Enter the lenght of the triangle"))
Area= Height * Base//2
#floor division rounds the result down to nearest whole number
print(f"The area of right angled triangle: {Area}")