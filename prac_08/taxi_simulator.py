from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

def main():
    total_fare = 0
    taxi_list = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive")
    print("q)uit, c)hoose taxi, d)rive")
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            display_taxi_list(taxi_list)
            taxi_number = choose_taxi(taxi_list)
        elif choice == "d":
            try:
                taxi_fare = start_drive(taxi_number, taxi_list)
                total_fare += taxi_fare
            except UnboundLocalError:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(total_fare))
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()
    print("Total trip cost: ${}".format(total_fare))
    print("Taxis are now:")
    display_taxi_list(taxi_list)

def display_taxi_list(taxi_list):
    x = -1
    for i in taxi_list:
        x += 1
        print("{} - {}".format(x, i))

def choose_taxi(taxi_list):
    taxi_choice = input("Choose taxi: ")
    if taxi_choice >= str(len(taxi_list)):
        print("Invalid taxi choice")
    return taxi_choice

def start_drive(taxi_number, taxi_list):
    taxi_drive = taxi_list[int(taxi_number)]
    distance = float(input("Drive how far? "))
    taxi_drive.start_fare()
    taxi_drive.drive(distance)
    print("Your Prius trip cost you ${:.2f}".format(taxi_drive.get_fare()))
    return taxi_drive.get_fare()








main()