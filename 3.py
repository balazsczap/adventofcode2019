from input_3 import main, test1, test2, test3


up = lambda current_position, length: (current_position[0], current_position[1] + length)
down = lambda current_position, length: (current_position[0], current_position[1] - length)
left = lambda current_position, length: (current_position[0] - length, current_position[1])
right = lambda current_position, length: (current_position[0] + length, current_position[1])

directions = {
    "U": up,
    "D": down,
    "L": left,
    "R": right
}
def task1_on_input(input):
    [line1, line2]= map(lambda line: line.split(","), input.split("\n"))

    def to_instructions(line):
        return map(lambda instruction: {"command":instruction[0], "length": int(instruction[1:])}, line)


    def step(current_position, instruction):
        return directions[instruction["command"]](current_position, instruction["length"])

    def interpolate(tuple1, tuple2, length):
        if tuple1[0] == tuple2[0]:
            start = tuple1[1]
            end = tuple2[1]
            step = (start - end) / abs(start - end)
            return zip([tuple1[0]]*(length+1), [start]+ range(start-step, end, -step) + [end])
        elif tuple1[1] == tuple2[1]:
            start = tuple1[0]
            end = tuple2[0]
            step = (start-end)/abs(start-end)
            return zip([start] + range(start -step, end, -step) + [end], [tuple1[1]] * (length+1) )
            
    def do_all_steps(line):
        all_positions = [(0,0)]
        current_position = (0, 0)
        print(line)
        for instruction in to_instructions(line):
            length = instruction["length"]
            last_position = current_position
            current_position = step(current_position, instruction)
            progressing_positions = interpolate(last_position, current_position, length)
            all_positions = all_positions  + progressing_positions[1:]
        return all_positions
            
    def find_intersections(steps1, line2):
        all_positions = [(0, 0)]
        intersections = []
        current_position = (0, 0)
        print(line2)
        for instruction in to_instructions(line2):
            length = instruction["length"]
            last_position = current_position
            current_position = step(current_position, instruction)
            progressing_positions = interpolate(last_position, current_position, length)

            for pos in progressing_positions:
                intersections = intersections + filter(lambda step: step[0] == pos[0] and step[1] == pos[1], steps1)

            all_positions = all_positions  + progressing_positions[1:]
        return [intersections, all_positions]
        
    steps1 = do_all_steps(line1)

    [intersections, steps2] = find_intersections(steps1, line2)
    # print(steps1)
    print(intersections)
    lowest = min(filter(lambda x: x>0, map(lambda x: x[0]+x[1], intersections)))
    print(lowest)
    # print(stesp2)
    # def find_same_steps(step, othersteps):
    #     return list(filter(lambda item: item[0] == step[0] and item[1] == step[1], othersteps))



    # matching_steps = filter(lambda x: len(x[1]) > 0, map(lambda step: (step, find_same_steps(step, steps2)), steps1))

    # total_distances = map(lambda matches: matches[0][0] + matches[0][1], matching_steps)
    # total_distances_except_zero = filter(lambda x: x>0, total_distances)
    # print(total_distances_except_zero)
    # lowest = min(total_distances_except_zero)
    # print(lowest)

task1_on_input(test1)
task1_on_input(test2)
task1_on_input(test3)
task1_on_input(main)
