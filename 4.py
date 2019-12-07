
import functools

def task1():
    valid_numbers = []
    for i in range(136760, 595730+1):
    # for i in range(136760, 136778):
        letters = list(str(i))
        numbers = map(lambda n: int(n), letters)
        (double, is_any_double) = functools.reduce(lambda acc, val: (acc[0] if acc[1] else val, acc[1] or acc[0] == val), numbers, (None, False))
        (_, is_increasing) = functools.reduce(lambda acc, val: (val, True if acc[0] == None else ((acc[0] <= val) and acc[1])), numbers, (None, True))
        if is_any_double and is_increasing:
            valid_numbers.append(i)
    print(valid_numbers)
    print(len(valid_numbers))

def task2():
    valid_numbers = []
    for i in range(136760, 595730+1):
    # for i in range(136760, 136778):
        letters = list(str(i))
        numbers = map(lambda n: int(n), letters)
        i = 0
        groups = {0:(-1,-1)}
        for l in numbers:
            if l == groups[i][0]:
                groups[i] = (l, groups[i][1]+1)
            else:
                i+=1
                groups[i] = (l, 1)
            
        doubles = map(lambda x: x[1][1] == 2, list(groups.items()))
        is_any_exactly_double = any(doubles)
        (_, is_increasing) = functools.reduce(lambda acc, val: (val, True if acc[0] == None else ((acc[0] <= val) and acc[1])), numbers, (None, True))
        if is_any_exactly_double and is_increasing:
            valid_numbers.append(i)

    print(valid_numbers)
    print(len(valid_numbers))


task2()