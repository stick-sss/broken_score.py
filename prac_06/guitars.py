from prac_06.guitar import Guitar

print("My Guitars")

def main():
    guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        add_guitar = Guitar(name, year, cost)
        print(f"{add_guitar}\n")
        guitars.append(add_guitar)
        name = input("Name: ")
    print("\n...snip...\n")
    print("These are my guitars:")

    i = 0
    for gita in guitars:
        if gita.is_vintage() == True:
            vintage_string = "(vintage)"
        else:
            vintage_string = ""
        i += 1
        print((f"Guitar {i}: {gita.name:>10} ({gita.year}), worth ${gita.cost:.2f} {vintage_string}"))

main()