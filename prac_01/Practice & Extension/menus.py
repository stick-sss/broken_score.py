name = input("Enter Name: ")
menu = '''(H)ello
(G)oodbye
(Q)uit'''
print(menu)
choice = input(">>> ")
while choice != "Q":
    if choice == "H":
        print(f"hello {name}")
    elif choice == "G":
        print(f"goodbye {name}")
    else:
        print("invalid message")
    print(menu)
    choice = input(">>> ")
print("Finished")