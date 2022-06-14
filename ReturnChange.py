# Projects from the following link
# https://github.com/karan/Projects

### CHANGE RETURN
# The user enters a cost and then the amount of money given.
# The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.

def calculateChange(price, money_given):
    """ Calculate how much change is needed

    :param price: decimal value of the price of the item
    :param money_given: decimal value of the money given to pay for item
    :return: float value for amount of change to return to customer
    """
    return float(money_given) - float(price)

def printCoinDict(coinDict):
    """ Formats and prints change neatly

    :param coinDict: dictionary of coin names and how many are to be given as change
    :return: nothing
    """
    for coin in coinDict.keys():
        number = coinDict[coin]
        print('{coin}: {number}'.format(coin=coin, number=number))

def calculateCoins(change):
    """ Create dictionary of coins needed for change

    :param change: decimal value of change to give
    :return: dictionary of coins with names as keys and amounts as values
    """
    coin_values = [100, 25, 10, 5, 1]
    coin_map = {100: 'Dollars', 25: 'Quarters', 10: 'Dimes', 5: 'Nickels', 1: 'Pennies'}
    coin_dict = {'Dollars': 100, 'Quarters': 0, 'Dimes': 0, 'Nickels': 0, 'Pennies': 0,}
    integer_change = int(change * 100)
    dummy_change = integer_change

    #while dummy_change > 0:
    for coin in coin_values:
        coins_needed = int(dummy_change / coin)
        dummy_change -= coin*coins_needed
        coin_dict[coin_map[coin]] = coins_needed

    return coin_dict

def main():
    test = True

    if not test:
        price = input('How much did the item cost? ')
        money_given = input('How much money did you give? ')
    else:
        price = 5.21
        money_given = 10
    # Calculate Change
    change_required = calculateChange(price, money_given)

    coins_needed = calculateCoins(change_required)
    print('CHANGE REQUIRED: ${change}'.format(change=change_required))
    printCoinDict(coins_needed)

    pass

if __name__ == '__main__':
    main()