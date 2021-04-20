# now the code raises an error and stops working when users input is incorrect
values_to_buy = {
    "USD": 27.9,
    "EUR": 33
}

values_to_sell = {
    "USD": 25.5,
    "EUR": 31
}


class BuySellError(Exception):
    pass


class CurrencyError(Exception):
    pass


class AmountOfMoneyError(Exception):
    pass


operation = (input("Do you want to buy or sell?"))
if operation == 'buy' or operation == 'sell':
    pass
else:
    raise BuySellError('Operation can be BUY or SELL only')


currency = (input("Input your currency:"))
if not currency in values_to_buy or not currency in values_to_sell:
    raise CurrencyError("There is no such currency")


amount_of_money = (input("Enter the amount of money:"))
if not amount_of_money.isdigit():
    raise AmountOfMoneyError('Please enter a correct amount of money')

if operation == "buy":
    print("You have to pay :", round(values_to_buy[currency] * int(amount_of_money), 2), 'hryvnas')
elif operation == "sell":
    print("You will get:", round(values_to_sell[currency] * int(amount_of_money), 2), 'hryvnas.')

