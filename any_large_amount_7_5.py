def change(amount):
    assert(amount <= 1000)
    if amount == 24:
        return [5, 5, 7, 7]
    if amount == 5:
        return [5]
    if amount == 7:
        return [7]
    if amount % 7 == 0:
        coins = change(amount - 7)
        coins.append(7)
        return coins
    else:
        coins = change(amount - 5)
        coins.append(5)
        return coins


def pretty_print(coins):
    total = 0
    for coin in coins:
        total = total + coin
    print("Solution is %s, verified amount total: %s" % (coins, total))


pretty_print(change(999))
