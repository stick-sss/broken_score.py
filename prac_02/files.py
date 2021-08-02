#(1)
name_file = open("name.txt","w")
name = input("Name: ")
print(f"{name}", file=name_file)
name_file.close()

#(2)
name_file = open("name.txt","r")
name = name_file.read()
print(f"Your name is {name}")
name_file.close()

#(3)
numbers_file = open("numbers.txt","r")
first_number = int(numbers_file.readline())
second_number = int(numbers_file.readline())
total = first_number + second_number
print(total)
numbers_file.close()

#(4)
numbers_file = open("numbers.txt","r")
total = 0
for all_numbers in numbers_file:
    numbers = int(all_numbers)
    total += numbers
print(total)
numbers_file.close()