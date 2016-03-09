# Uses python3
"""
Computes minimal number of coins necessary to return from money to be changed
for given denomination
"""
import sys


def main():
    money_to_change = int(sys.stdin.read())
    print(get_change(money_to_change))


def get_change(money_to_change):
    number_of_coins = 0
    while money_to_change > 0:
        money_to_change, number_of_coins = if_possible_change(money_to_change, number_of_coins, 10)
        money_to_change, number_of_coins = if_possible_change(money_to_change, number_of_coins, 5)
        money_to_change, number_of_coins = if_possible_change(money_to_change, number_of_coins, 1)
    return number_of_coins


def if_possible_change(money_to_change, number_of_coins, denomination):
    while money_to_change - denomination >= 0:
        money_to_change -= denomination
        number_of_coins += 1
    return money_to_change, number_of_coins


if __name__ == '__main__':
    main()
