import re
from collections import defaultdict
from itertools import product


class Computer:
    def __init__(self, a, b, c, input):
        self.init_a = int(a)
        self.init_b = int(b)
        self.init_c = int(c)
        self.code = self.parse_input(input)

        self.init_state()

    def init_state(self):
        self.a = self.init_a
        self.b = self.init_b
        self.c = self.init_c
        self.pc = 0
        self.output = []

    def print_output(self):
        print(",".join(map(str, self.output)))

    def run(self, a=None, max_output_length=None):
        self.init_state()
        if a:
            self.a = a
        while self.exec():
            if max_output_length and len(self.output) >= max_output_length:
                return

    def parse_input(self, input):
        code = list(map(int, input.split(",")))
        return code

    def exec(self):
        if self.pc >= len(self.code) - 1:
            return False
        opcode, operand = self.code[self.pc], self.code[self.pc + 1]
        match opcode:
            case 0:
                self.adv(operand)
            case 1:
                self.bxl(operand)
            case 2:
                self.bst(operand)
            case 3:
                self.jnz(operand)
            case 4:
                self.bxc(operand)
            case 5:
                self.out(operand)
            case 6:
                self.bdv(operand)
            case 7:
                self.cdv(operand)
        self.pc += 2
        return True

    def _combo_op(self, value):
        if value <= 3:
            return value
        if value == 4:
            return self.a
        if value == 5:
            return self.b
        if value == 6:
            return self.c

    def dv(self, n):
        return self.a >> self._combo_op(n)

    def adv(self, n):
        self.a = self.dv(n)

    def bxl(self, n):
        self.b ^= n

    def bst(self, n):
        self.b = self._combo_op(n) % 8

    def jnz(self, n):
        if self.a == 0:
            return
        self.pc = n - 2

    def bxc(self, n):
        self.b ^= self.c

    def out(self, n):
        self.output.append(self._combo_op(n) % 8)

    def bdv(self, n):
        self.b = self.dv(n)

    def cdv(self, n):
        self.c = self.dv(n)


def main():
    with open("input.txt", "r") as f:
        input = f.read()

        f = re.findall(
            r"Register A: (\d+)\nRegister B: (\d+)\nRegister C: (\d+)\n\nProgram: (.*)\n",
            input,
            re.MULTILINE,
        )[0]

        # part 1
        program = f[3]
        expected_output = list(map(int, program.split(",")))
        c = Computer(*f)
        i = 1
        c.run()
        c.print_output()

        # part 2
        output_to_possible_inputs = defaultdict(list)
        for i in range(1, 1 << 10):
            c.run(a=i, max_output_length=1)
            out = c.output
            if out:
                output_to_possible_inputs[out[0]].append(i)

        possible_nums = set()
        for input in output_to_possible_inputs[expected_output[0]]:
            possible_nums.add(input)

        current_shift = 3
        for output in expected_output[1:]:
            possible_inputs = output_to_possible_inputs[output]
            new_possible_nums = set()
            for input, num in product(possible_inputs, possible_nums):
                a = num >> current_shift
                b = input & ((1 << 7) - 1)
                if a == b:
                    prefix = input >> 7
                    new_num = num | (prefix << (7 + current_shift))
                    new_possible_nums.add(new_num)
            possible_nums = new_possible_nums
            current_shift += 3

        print(min(possible_nums))


if __name__ == "__main__":
    main()
