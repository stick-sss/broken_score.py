from prac_08.unreliable_car import UnreliableCar

def main():
    test_car_i = UnreliableCar("Oppressor Mk II", 200, 90)
    test_car_ii = UnreliableCar("Oppressor Mk II", 200, 10)
    test_car_i.drive(120)
    test_car_ii.drive(50)
    print(test_car_i)
    print(test_car_ii)

main()
