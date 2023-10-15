from forex_python.converter import CurrencyRates


cr = CurrencyRates()

amount = int(input("Enter the amount you want to convert: "))

fromCurr = input("Enter from which currency you want to convert: ").upper()

toCurr = input("Enter the currency you want to convert to: ").upper()

print(f"You want to convert {amount} from {fromCurr} to {toCurr}")

output = cr.convert(fromCurr, toCurr, amount)

print(f"The converted amount is {output}")