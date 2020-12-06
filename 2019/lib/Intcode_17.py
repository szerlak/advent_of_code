from collections import defaultdict, deque
from copy import copy


class ModeValueError(Exception):
    pass


class NoInputException(Exception):
    pass


class Intcode:

    def __init__(self, program, *, setting=None, debug=False):
        self.setting = setting
        self.cursor = 0
        self.debug = debug
        self.relative_base = 0
        self.input = None
        self.is_running = True
        self.output = None

        self.OPCODE = {
            1: self._ADD,
            2: self._MULTI,
            3: self._INPUT,
            # 4: self._OUTPUT,
            5: self._JUMP_TRUE,
            6: self._JUMP_FALSE,
            7: self._LESS,
            8: self._EQUAL,
            9: self._SET_RELATIVE_BASE
            # 99: self._EXIT
        }

        self.program = defaultdict(int)
        for i, p in enumerate(program):
            self.program[i] = p

        if setting:
            self.set_value(1, setting)
            self.cursor += 2

    def __str__(self):
        return str(self.setting)

    def log(self, *args):
        if self.debug:
            print(*args)

    def clone(self):
        new_computer = Intcode(
            [],
            debug=self.debug,
            setting=self.setting
        )
        new_computer.cursor = self.cursor
        new_computer.relative_base = self.relative_base
        new_computer.input = self.input
        new_computer.is_running = self.is_running
        new_computer.output = self.output
        new_computer.program = copy(self.program)
        return new_computer

    def set_input(self, input=[]):
        self.input=deque(input)

    def set_data(self, data=""):
        commands = []
        for line in data.splitlines():
            commands += map(ord, line)
            commands.append(ord("\n"))

        self.input = deque(commands)

    def run(self, input=[]):
        if input:
            self.input = deque(input)

        while True:
            opcode = self.get_opcode()
            if opcode == 4:
                # print("_OUTPUT", self.cursor)
                output = self.get_value(1)
                self.cursor += 2
                return output
            if opcode == 99:
                self.is_running = False
                break
            self.OPCODE[opcode]()
        return None

    def get_opcode(self):
        return self.program[self.cursor] % 100

    def get_mode(self, n):
        if n == 0:
            raise ModeValueError
        instruction = str(self.program[self.cursor]).zfill(5)
        mode = list(map(int, list(instruction[:3])))
        mode.reverse()
        return mode[n-1]

    def set_value(self, n, value):
        self.program[self._get_index(n)] = value

    def get_value(self, n):
        return self.program.get(self._get_index(n), 0)

    def _get_index(self, n):
        mode = self.get_mode(n)
        if mode == 0:
            return self.program[self.cursor + n]
        if mode == 1:
            return self.cursor + n
        if mode == 2:
            return self.relative_base + self.program[self.cursor + n]
        raise ValueError("Wrong mode value")

    def _ADD(self):
        self.log("_ADD: ", self.cursor)
        self.set_value(3, self.get_value(1) + self.get_value(2))
        self.cursor += 4

    def _MULTI(self):
        self.log("_MULTI: ", self.cursor)
        self.set_value(3, self.get_value(1) * self.get_value(2))
        self.cursor += 4

    def _INPUT(self):
        self.log("_INPUT", self.cursor)
        # print("_INPUT", self.cursor)
        if not self.input:
            raise NoInputException
        self.set_value(1, self.input.popleft())
        # self.input = None
        self.cursor += 2

    def _OUTPUT(self):
        self.log("_OUTPUT", self.cursor)
        # print("_OUTPUT", self.cursor)
        output = self.get_value(1)
        self.cursor += 2
        return output

    def _JUMP_TRUE(self):
        self.log("_JUMP_TRUE", self.cursor)
        self.cursor = self.get_value(2) if self.get_value(1) != 0 else self.cursor + 3

    def _JUMP_FALSE(self):
        self.log("_JUMP_FALSE", self.cursor)
        self.cursor = self.get_value(2) if self.get_value(1) == 0 else self.cursor +3

    def _LESS(self):
        self.log("_LESS", self.cursor)
        self.set_value(3, 1 if self.get_value(1) < self.get_value(2) else 0)
        self.cursor += 4

    def _EQUAL(self):
        self.log("_EQUAL", self.cursor)
        self.set_value(3, 1 if self.get_value(1) == self.get_value(2) else 0)
        self.cursor += 4

    def _SET_RELATIVE_BASE(self):
        self.log("_SET_RELATIVE_BASE", self.cursor)
        self.relative_base += self.get_value(1)
        self.cursor += 2

    def _EXIT(self, _):
        self.log("EXIT")
