"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""
choice = input("Choose currency to convert(1 = THB to USD, 2 = USD to THB): ")

if choice == "1":
    amount = float(input("Enter amount THB: "))
    result = amount / 35.5

    print(f"{amount} THB / 35.5 = {result:.2f} USD")

elif choice == "2":
    amount = float(input("Enter amount USD: "))
    result = amount * 35.5

    print(f"{amount} USD * 35.5 = {result:.2f} THB")

else:
    print("Invalid choice")
