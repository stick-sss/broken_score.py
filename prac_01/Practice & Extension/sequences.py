menu = '''i. Show the even numbers from x to y
ii. Show the odd numbers from x to y
iii. Show the squares from x to y
iv. Exit the program'''
x = int(input("X: "))
y = int(input("Y: "))
print(menu)
choice = input(">>> ")
while choice != "iv":
    if choice == "i":
        for i in range(x,y):
            if i % 2 == 0:
                print(i,end=" ")
    elif choice == "ii":
        for i in range(x,y):
            if i % 2 == 1:
                print(i,end=" ")
    elif choice == "iii":
        for i in range(x, y):
            squares = i*i
            print(squares,end=" ")
    else:
        print("Invalid Enter")
    print()
    print(menu)
    choice = input(">>> ")
print("Thank you")
