def main():
    picks = number_of_picks()
    quick_pick(picks)

def number_of_picks():
    number = int(input("How many quick picks? "))
    return number

def quick_pick(picks):
    import random
    for i in range(picks):
        constants = []
        for x in range(6):
            pick_number = random.randint(1,45)
            while pick_number in constants:
                pick_number = random.randint(1, 45)
            constants.append(pick_number)
        constants.sort()
        print(" ".join("{:2}".format(number) for number in constants))

main()