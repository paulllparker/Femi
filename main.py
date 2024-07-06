

print("Welcome to the currency converter toolkit made by Paul Parker.")

exchange_rate = 210
currency = input("What currency do you which to change (Naira or RMB)?"
                 "\nType (N) for Naira or (R) for RMB: ")
currency = currency.upper()
amount = float(input("How much do you wish to change: "))
total_rmb = amount * exchange_rate
total_naira = amount / exchange_rate
while amount <= 0:
    print("You must enter a positive number")
    amount = float(input("How much do you wish to change: "))

if currency == "N":
    print(f"₦{amount:,.2f} = ¥{total_naira:,.2f}")
    decision = input("Press q to quit :")

elif currency == "R":
    print(f"¥{amount:,.2f} = ₦{total_rmb:,.2f}")
    decision = input("Press q to quit :")


else:
    print(f"{currency} is a wrong input. Please try again!")
    decision = input("Press q to quit :")

while not decision == "q":
    decision = input("Press q to quit :")
print("Bye")

