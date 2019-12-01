import math
from functools import reduce

from input_1 import task_input


def calculate_fuel(mass):
  return math.floor(mass / 3) - 2

fuels = map(lambda x: calculate_fuel(int(x)), task_input.splitlines())
result = reduce(lambda acc, val: acc + val, fuels)

print(result)