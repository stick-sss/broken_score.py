for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0,101,10):
    print(i, end=" ")
print()

for i in range(20,0,-1):
    print(i, end=" ")
print()

x = int(input("Number of stars: "))
for i in range(x):
    print("*", end="")
print()

for i in range(x+1):
    print("*"*i)