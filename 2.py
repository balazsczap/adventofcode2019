from input_2 import main, test1, test2, test3, test4

class IntComputer():
    def __init__(self):
        self.memory = []
        self.memory_pointer = 0


        self.bytesize = 4
        self.input = None
        
        self.output_func = lambda x: print(x)
        
        self.running = True

    def set_memory(self, memory):
        self.memory = memory

    def add_stdin(self, input_func):
        self.input = input_func

    def get_stdout(self, output_func):
        return output_func

    def add_stdout(self, output_func):
        self.output_func = output_func

    def read_stdin(self):
        if self.input != None:
            return self.input()

    def add(self, x, y):
        return x + y

    def multiply(self, x, y):
        return x * y

    def jump(self, x):
        self.memory_pointer = x

    def stop(self, *args):
        self.running = False

    def start(self):
        self.running = True
        self.loop()

    def get_current_byte(self):
        return self.memory[self.memory_pointer : self.memory_pointer + self.bytesize]

    def get_parameter_values(self, parameters, parameter_modes):
        def get_value(i):
            param = parameters[i]
            mode = parameter_modes[i]
            if mode == 'IMMEDIATE_MODE':
                return param
            elif mode == 'POSITION_MODE':
                return self.memory[param]

        return [get_value(i) for i in range(0, len(parameters)-1)] + [0] 

    def loop(self):
        while (self.running == True):
            byte = self.get_current_byte()
            [instruction, *parameters] = byte
            command = self.parse_command(instruction)
            parameter_modes = self.parse_parameter_modes(instruction, len(parameters))
            parameter_values = self.get_parameter_values(parameters, parameter_modes)
            
            result = command(*(parameter_values[:-1]))
            if result != None:
                memory[parameters[-1]] = result

            self.jump(self.memory_pointer+self.bytesize)

            

    def parse_command(self, instruction):
        command_number = instruction % 100
        if command_number == 1:
            return self.add
        if command_number == 2:
            return self.multiply
        elif command_number == 99:
            return self.stop
        else: raise Exception('invalid command: ' + str(command_number))

    def parse_parameter_mode(self, number):
        if number == 1:
            return 'IMMEDIATE_MODE'
        else:
            return 'POSITION_MODE'


    def parse_parameter_modes(self, instruction, number_of_parameters):
        parameter_modes = [int(d) for d in str(instruction)[0:-2].rjust(number_of_parameters, '0')]
        return list(map(self.parse_parameter_mode, parameter_modes))
        

def parse_instructions(inputstring):
    return list(map(lambda x: int(x),  inputstring.split(',')))


computer = IntComputer()

memory = parse_instructions(main)
memory[1] = 12
memory[2] = 2

computer.set_memory(memory)
computer.start()
print(memory)