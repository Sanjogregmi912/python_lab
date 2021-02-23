# N students take  K apples and distribute them among each other evenly. the remaining (the undivisible)part reamins in the basket .how many apples will each single students get? how many apples will remain in the basket? the program reads the number N and K. It should print the two answer for question above
N=int(input("enter the number of students:"))
K=int(input("enter the number of apples:"))
t=K//N
n=K%N
print(f"the number of apples that students gets: {t}")
print(f"the number of remaining apples: {n}")