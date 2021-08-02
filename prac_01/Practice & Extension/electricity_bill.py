print("Electricity bill estimator 2.0")
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
price_kWh = float(input("Which tariff? 11 or 31: "))
use_kWh = float(input("Enter daily use in kWh: "))
day = int(input("Enter number of billing days: "))
if price_kWh == 11:
    bill = TARIFF_11 * use_kWh * day
elif price_kWh == 31:
    bill = TARIFF_31 * use_kWh * day
else:
    print("Invalid Enter")
print(f"Estimated bill: ${bill:.2f}")