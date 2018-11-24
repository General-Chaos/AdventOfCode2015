import re


class InstructionSet:

    def __init__(self, a, b, instructions):
        self.a = a
        self.b = b
        self.instructions = instructions
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index not in range(0, len(self.instructions)):
            raise StopIteration
        else:
            current = (self.a, self.b)
            self._process_current_instruction()
            return current

    def _process_current_instruction(self):
        instruction = self.instructions[self.current_index]
        if re.match("^inc", instruction):
            self._inc_register(instruction)
            self.current_index += 1
        elif re.match("^tpl", instruction):
            self._tpl_register(instruction)
            self.current_index += 1
        elif re.match("^hlf", instruction):
            self._hlf_register(instruction)
            self.current_index += 1
        elif re.match("^jmp", instruction):
            offset = self._get_jmp_offset(instruction)
            self.current_index += offset
        else:
            offset = self._get_ji_offset(instruction)
            self.current_index += offset

    def _inc_register(self, instruction):
        register = instruction.split(" ")[1]
        if register == "a":
            self.a += 1
        else:
            self.b += 1

    def _tpl_register(self, instruction):
        register = instruction.split(" ")[1]
        if register == "a":
            self.a *= 3
        else:
            self.b *= 3

    def _hlf_register(self, instruction):
        register = instruction.split(" ")[1]
        if register == "a":
            self.a = int(round(self.a / 2))
        else:
            self.b = int(round(self.b / 2))

    def _get_jmp_offset(self, instruction):
        split = instruction.split(" ")
        number = int(split[1][1:])
        sign = split[1][0]
        if sign == "-":
            return (-1 * number)
        else:
            return number

    def _get_ji_offset(self, instruction):
        split = instruction.split(", ")
        instruction_split = split[0].split(" ")
        ji_instruction = instruction_split[0]
        register = instruction_split[1]
        number = int(split[1][1:])
        sign = split[1][0]

        if ji_instruction == 'jio':
            if register == "a":
                if self.a == 1:
                    if sign == "-":
                        return (-1 * number)
                    else:
                        return number
                else:
                    return 1
            else:
                if self.b == 1:
                    if sign == "-":
                        return (-1 * number)
                    else:
                        return number
                else:
                    return 1
        else:
            if register == "a":
                if (self.a % 2) == 0:
                    if sign == "-":
                        return (-1 * number)
                    else:
                        return number
                else:
                    return 1
            else:
                if (self.b % 2) == 0:
                    if sign == "-":
                        return (-1 * number)
                    else:
                        return number
                else:
                    return 1
