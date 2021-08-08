def main():
    numbers = get_number()
    print_numbers(numbers)
    authorised_users()

def get_number():
    numbers = []
    for i in range(5):
        number = int(input("Number: "))
        numbers.append(number)
    return numbers

def print_numbers(numbers):
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    numbers.sort()
    print("The smallest number is {}".format(numbers[0]))
    print("The largest number is {}".format(numbers[-1]))
    print("The average of the number is {}".format(sum(numbers)/len(numbers)))

def authorised_users():
    print()
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    name = input("Username: ")
    if name in usernames:
        print("Access granted")
    else:
        print("Acess denied")

main()