from prac_08.silver_service_taxi import SilverServiceTaxi

def main():
    test_taxi = SilverServiceTaxi("BMW M3", 100, 2)
    test_taxi.drive(18)
    print(test_taxi)
    print(f"fare: ${test_taxi.get_fare():.2f}")

main()
