"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def main():
    score = get_score()
    grade = get_grade(score)
    random = get_random()
    print(grade)
    print(random)

def get_score():
    score = float(input("Enter score: "))
    return score

def get_grade(score):
    if score < 0:
        return "Invalid score"
    elif score > 100:
        return "Invalid score"
    elif score >= 50 and score < 90:
        return "Passable"
    elif score >= 90:
        return "Excellent"
    elif score < 50:
        return "Bad"

def get_random():
    import random
    number = random.randint(0,100)
    return number

main()