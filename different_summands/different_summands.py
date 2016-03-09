"""
Uses python3

Represent  a  given  positive  integer n
as  a  sum  of  as  many  pairwise distinct positive integers as possible

"""
import sys


def main():
    target_value = initialize_data()
    summands = optimal_summands(target_value)
    print_output(summands)


def initialize_data():
    input_data = sys.stdin.read()
    return int(input_data)


def optimal_summands(target_value):
    summands = []
    current_val_to_add = 1
    current_sum = 0
    while current_val_to_add+current_sum != target_value:
        current_sum, current_val_to_add, summands = \
            chose_to_append_or_increment_value(current_sum, current_val_to_add, target_value, summands)
    summands.append(current_val_to_add)
    return summands


def chose_to_append_or_increment_value(current_sum, current_val_to_add, target_value, summands):
    if (current_sum+1)+(2*current_val_to_add) <= target_value:
        summands.append(current_val_to_add)
        current_sum += current_val_to_add
        current_val_to_add += 1
    elif current_sum + current_val_to_add < target_value:
        current_val_to_add += 1
    return current_sum, current_val_to_add, summands


def print_output(summands):
    print("number of pairwise distinct numbers:", len(summands))
    print("founded numbers:", end=' ')
    for x in summands:
        print(x, end=' ')


if __name__ == '__main__':
    main()
