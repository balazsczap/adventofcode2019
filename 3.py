from input_3 import main, main_short, test1, test2, test3

import time


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
        
def is_point_on_line(point, section):
    return (point[0] - section[0][0])*(section[1][1] - section[0][1]) - (point[1]-section[0][1])*(section[1][0] - section[0][0])

def order_section(section):
    if (section[0][0] > section[1][0] or section[0][1] > section[1][1]):
        return (section[1], section[0])
    return section

def is_crossing(section1, section2):
    ordered_section1 = order_section(section1)
    ordered_section2 = order_section(section2)
    
    section2_start_on_line = is_point_on_line(ordered_section2[0], ordered_section1)
    section2_end_on_line = is_point_on_line(ordered_section2[1], ordered_section1)

    section1_start_on_line = is_point_on_line(ordered_section1[0], ordered_section2)
    section1_end_on_line = is_point_on_line(ordered_section1[1], ordered_section2)
    
    return section1_start_on_line * section1_end_on_line < 0 and section2_start_on_line * section2_end_on_line < 0


def create_sections(line):
    sections = []
    current_position = (0, 0)
    for instruction in to_instructions(line):
        length = instruction["length"]
        last_position = current_position
        current_position = step(current_position, instruction)
        sections.append((last_position, current_position))
    return sections

def task1_on_input(input):
    [line1, line2]= map(lambda line: line.split(","), input.split("\n"))

            
    def find_intersections(sections, line2):
        all_positions = [(0, 0)]
        intersections = []
        current_position = (0, 0)
        for instruction in to_instructions(line2):
            length = instruction["length"]
            last_position = current_position
            current_position = step(current_position, instruction)
            print((last_position, current_position))
            

            intersecting_sections = filter(lambda x: is_crossing(x, (last_position, current_position)), sections)
            
            progressing_positions = interpolate(last_position, current_position, length)
            for pos in progressing_positions:
                for section in intersecting_sections:
                    if is_point_on_line(pos, section) == 0:
                        intersections.append(pos)

        return intersections
        

    sections = create_sections(line1)
    print(sections)
    intersections = find_intersections(sections, line2)
    print(intersections)
    
    lowest = min(filter(lambda x: x>0, map(lambda x: abs(x[0])+abs(x[1]), filter(lambda x: x[0]!=0 and x[1]!=0, intersections))))
    print(lowest)

def task2_on_input(input):
    start = time.time()

    [line1, line2] = map(lambda line: line.split(","), input.split("\n"))
        
    def find_intersections(sections, line2):
        all_positions = [(0, 0)]
        intersections = []
        current_position = (0, 0)
        # print("line2")
        all_lengths = 0
        for instruction in to_instructions(line2):
            length = instruction["length"]
            last_position = current_position
            current_position = step(current_position, instruction)
            

            intersecting_sections = filter(lambda x: is_crossing(x, (last_position, current_position)), sections)
            
            progressing_positions = interpolate(last_position, current_position, length)
            for pos in progressing_positions:
                for section in intersecting_sections:
                    if is_point_on_line(pos, section) == 0:
                        intersections.append((pos, all_lengths + progressing_positions.index(pos)))
                        
            all_lengths+=length
        return intersections
        
        

    sections1 = create_sections(line1)
    sections2 = create_sections(line2)
    # print(sections1)
    # print(sections2)
    intersections1 = filter(lambda x: x[0]!=0 and x[1]!=0, find_intersections(sections1, line2))
    intersections2 = filter(lambda x: x[0]!=0 and x[1]!=0, find_intersections(sections2, line1))
    # print(intersections1)
    # print(intersections2)

    def orderbycoords(list):
        return sorted(list, key=lambda k: (k[0], k[1]))

    zipped = zip(orderbycoords(intersections1), orderbycoords(intersections2))
    # print(zipped)
    sum_dist = map(lambda x: x[0][1] + x[1][1], zipped)
    # print(sum_dist)
    result = min(filter(lambda x: x > 0, sum_dist))
    print(result)
    end = time.time()
    print(end - start)

    # lowest = min(filter(lambda x: x>0, map(lambda x: abs(x[0])+abs(x[1]), filter(lambda x: x[0]!=0 and x[1]!=0, intersections))))
    # print(lowest)



# task1_on_input(test1)
# task1_on_input(test2)
# task1_on_input(test3)
# task1_on_input(main)


# task2_on_input(test1)
# task2_on_input(test2)
# task2_on_input(test3)
task2_on_input(main)
# task2_on_input(main_short)
