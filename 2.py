from input_2 import main, test1, test2, test3, test4

def parse_command(number):
    if number == 1:
        return lambda x, y: x+ y
    if number == 2:
        return lambda x, y: x *y
    elif number == 99:
        return None
    else: raise Exception('invalid command ' + number)

def run_command(pos1, pos2, command, array):
    return command(array[pos1], array[pos2]) 

def run_iteration(index, array):
    number= array[index]
    command = parse_command(number)
    if command == None:
        return None
    [pos1, pos2, pos_out]= array[index+1:index+4]
    result = run_command(pos1, pos2, command, array)
    new_array = array.copy()
    new_array[pos_out] = result
    return new_array


    
def task_1():
    new_array[1] = 12
    new_array[2] = 2

    array = list(map(lambda x: int(x),  main.split(',')))
    index = 0
    new_array = array.copy()

    while new_array != None:
        array = new_array
        new_array = run_iteration(index, array)
        index += 4


def task_2():
    for noun in range(0, 99):
        for verb in range(0, 99):


            array = list(map(lambda x: int(x),  main.split(',')))
            index = 0
            new_array = array.copy()
            
            new_array[1] = noun
            new_array[2] = verb

            while new_array != None:
                array = new_array
                new_array = run_iteration(index, array)
                index += 4
            
            if array[0] == 19690720:
                print(noun * 100 + verb)
                

task_2()