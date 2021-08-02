"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

def main():
    sales = float(input("Enter sales: $"))
    while sales >= 0:
        bonus = bonus_calculation(sales)
        print(f"{bonus}")
        sales = float(input("Enter sales: $"))
    print("good bye")

def bonus_calculation(sales):
    if sales < 1000:
        bouns = sales * 0.1
    elif sales >= 1000:
        bouns = sales * 0.15
    return bouns

main()