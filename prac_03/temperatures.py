"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
def main():
    menu()
    choice = get_choice()
    while choice != "Q":
        if choice == "C":
            celsius = get_celsius()
            result = celsius_to_fahrenheit(celsius)
            calculator_result(result)
        elif choice == "F":
            fahrenheit = get_fahrenheit()
            result = fahrenheit_to_celsius(fahrenheit)
            calculator_result(result)
        else:
            Invalid_option()
        menu()
        choice = get_choice()
    program_end()


def program_end():
    print("Thank you.")

def menu():
    MENU ="""
C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit
"""
    print(MENU)

def get_choice():
    choice = input(">>> ").upper()
    return choice

def get_celsius():
    celsius = float(input("Celsius: "))
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

def get_fahrenheit():
    fahrenheit = float(input("Fahrenheit: "))
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius

def Invalid_option():
    print("Invalid option")

def calculator_result(result):
    print("Result: {:.2f} F".format(result))

main()