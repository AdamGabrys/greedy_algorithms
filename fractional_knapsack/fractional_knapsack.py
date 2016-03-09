"""
Uses python3

Resolve Fractional Knapsack problem for positive integer values. Returns most optimal value of elements in knapsack

Input Format:
The First line of the input contains the number n of items and the capacity W of a knapsack.
The next n lines determine the values and weights of the items.

weights > 0

"""

import sys
import random


def main():
    data = list(map(int, sys.stdin.read().split()))
    number_of_elements, capacity, elements = extract_data(data)
    opt_value = get_optimal_value(capacity, elements)
    print("{:.4f}".format(opt_value))


def extract_data(data):
    number_of_elements, capacity = data[0:2]
    elements = zip_backpack_elements(data, number_of_elements)
    return number_of_elements, capacity, elements


def zip_backpack_elements(data, number_of_elements):
    values = data[2:(2 * number_of_elements + 2):2]
    weights = data[3:(2 * number_of_elements + 2):2]
    elements = list(zip(values, weights))
    return elements


def get_optimal_value(capacity, elements):
    knapsack_value, knapsack_weight, elements = initialize_backpack(elements)
    while knapsack_weight < capacity and elements:
        element = elements.pop(0)
        knapsack_value, knapsack_weight = insert_to_back(element, knapsack_value, knapsack_weight, capacity)
    return knapsack_value


def initialize_backpack(elements):
    knapsack_value = 0.
    knapsack_weight = 0
    elements = sorted(elements, key=lambda weight_value: (weight_value[0]/weight_value[1]), reverse=True)
    return knapsack_value, knapsack_weight, elements


def insert_to_back(element, knapsack_value, knapsack_weight, capacity):
    if knapsack_weight + element[1] <= capacity:
        knapsack_value, knapsack_weight = insert_intact_element(element, knapsack_value, knapsack_weight)
    else:
        knapsack_value, knapsack_weight = insert_element_fraction(element, knapsack_value, knapsack_weight, capacity)
    return knapsack_value, knapsack_weight


def insert_intact_element(element, knapsack_value, knapsack_weight):
    knapsack_weight += element[1]
    knapsack_value += element[0]
    return knapsack_value, knapsack_weight


def insert_element_fraction(element, knapsack_value, knapsack_weight, capacity):
    maximal_weight = capacity-knapsack_weight
    knapsack_value += (maximal_weight/element[1])*element[0]
    knapsack_weight += maximal_weight
    return knapsack_value, knapsack_weight


if __name__ == "__main__":
    main()
