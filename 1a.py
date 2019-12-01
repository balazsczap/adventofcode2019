import math
from functools import reduce

from input_1 import task_input

def calculate_basic_fuel(mass):
    return math.floor(mass / 3) - 2

def add_extra_fuel(extra):
    new_fuel = calculate_basic_fuel(extra)
    if (new_fuel <= 0):
        return 0
    return new_fuel + add_extra_fuel(new_fuel)


def calculate_all_fuel(mass):
    initial_fuel = math.floor(mass / 3) - 2
    return initial_fuel + add_extra_fuel(initial_fuel)

fuels = map(lambda x: calculate_all_fuel(int(x)), task_input.splitlines())
result = reduce(lambda acc, val: acc + val, fuels)

print(result)