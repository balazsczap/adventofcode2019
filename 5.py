from input_5 import main, test1, test2

class IntComputer():
    def __init__(self):
        self.memory = []
        self.memory_pointer = 0


        self.input_func = None
        
        self.output_func = lambda x: print(x)
        
        self.running = True

    def set_memory(self, memory):
        self.memory = memory

    def add_stdin(self, input_func):
        self.input_func = input_func

    def get_stdout(self, output_func):
        return output_func

    def add_stdout(self, output_func):
        self.output_func = output_func

    def read_stdin(self):
        if self.input_func != None:
            return self.input_func()

    def write_stdout(self, value):
        if self.output_func != None:
            self.output_func(value)

    def add(self, x, y):
        return x + y

    def multiply(self, x, y):
        return x * y

    def input(self, position):
        self.memory[position]=self.read_stdin()

    def output(self, position):
        value = self.memory[position]
        self.write_stdout(value)

    def jump(self, x):
        self.memory_pointer = x

    def stop(self, *args):
        self.running = False

    def start(self):
        self.running = True
        self.loop()

    def get_current_byte(self, size):
        return self.memory[self.memory_pointer : self.memory_pointer + size]

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
            bytestart = self.memory[self.memory_pointer]
            (size, command) = self.parse_command(bytestart)
            byte = self.get_current_byte(size)
            if len(byte) > 1:
                [instruction, *parameters] = byte
            else:
                [instruction] = byte
                parameters = []
            parameter_modes = self.parse_parameter_modes(instruction, len(parameters))
            parameter_values = self.get_parameter_values(parameters, parameter_modes)
            
            real_param_values = parameter_values[:-1] if size > 2 else parameter_values
            result = command(*(real_param_values))

            # if parameter_modes[-1] == 'IMMEDIATE_MODE':
            #     self.output_func(str(parameter_values) + " : " + str(result)) # ???????????????????????????????????????????????????????????????
            # else:
            if result != None:
                memory[parameters[-1]] = result

            self.jump(self.memory_pointer+size)
        

    def parse_command(self, instruction):
        command_number = instruction % 100
        if command_number == 1:
            return (4, self.add)
        if command_number == 2:
            return (4, self.multiply)
        if command_number == 3:
            return (2, self.input)
        if command_number == 4:
            return (2, self.output)
        else:
            return (1, self.stop)
        # else: raise Exception('invalid command: ' + str(command_number))

    def parse_parameter_mode(self, number):
        if number == 1:
            return 'IMMEDIATE_MODE'
        else:
            return 'POSITION_MODE'


    def parse_parameter_modes(self, instruction, number_of_parameters):
        parameter_modes = [int(d) for d in str(instruction)[0:-2].rjust(number_of_parameters, '0')]
        parameter_modes.reverse()
        return list(map(self.parse_parameter_mode, parameter_modes))
        

def parse_instructions(inputstring):
    return list(map(lambda x: int(x),  inputstring.split(',')))

computer = IntComputer()

memory = parse_instructions(main)
computer.set_memory(memory)

stdin_buffer = [1]
def stdin():
    return stdin_buffer.pop(0)
computer.add_stdin(stdin)

stdout_buffer = []
def stdout(value):
    stdout_buffer.append(value)
computer.add_stdout(stdout)

computer.start()

print(stdout_buffer)

