class Intcode:

    def __init__(self, program, setting, debug=False):
        self.program = program.copy()
        self.setting = setting
        self.cursor = 0
        self.input_cursor = 0
        self.debug = debug
        self.output = []

        self.OPCODE = {
            1: self._ADD,
            2: self._MULTI,
            3: self._INPUT,
            4: self._OUTPUT,
            5: self._JUMP_TRUE,
            6: self._JUMP_FALSE,
            7: self._LESS,
            8: self._EQUAL,
            99: self._EXIT
        }

    def __str__(self):
        return str(self.setting)

    def log(self, *args):
        if self.debug:
            print(*args)

    def run(self, input):
        self.input = input
        # self.output = []
        finish = False

        while True:
            opcode, mode = self._get_instruction(self.cursor)
            self.OPCODE[opcode](mode)
            if opcode == 4:
                break
            if opcode == 99:
                finish = True
                break

        # self.log(self.program[0])
        return finish, self.output[-1]

    def _get_instruction(self, cursor):
        instruction = str(self.program[cursor]).zfill(5)
        opcode = int(instruction[-2:])
        mode = list(map(int, list(instruction[:3])))
        mode.reverse()
        return opcode, mode

    def _get_value(self, cursor, mode):
        if mode == 0:
            return self.program[self.program[cursor]]
        return self.program[cursor]

    def _ADD(self, mode):
        self.log("_ADD: ", self.cursor, mode)
        v1 = self._get_value(self.cursor + 1, mode[0])
        v2 = self._get_value(self.cursor + 2, mode[1])
        self.program[self.program[self.cursor+3]] = v1 + v2
        self.cursor += 4

    def _MULTI(self, mode):
        self.log("_MULTI: ", self.cursor, mode)
        v1 = self._get_value(self.cursor + 1, mode[0])
        v2 = self._get_value(self.cursor + 2, mode[1])
        self.program[self.program[self.cursor+3]] = v1 * v2
        self.cursor += 4

    def _INPUT(self, _):
        self.log("_INPUT", self.cursor)
        value = self.setting if self.input_cursor == 0 else self.input
        self.program[self.program[self.cursor + 1]] = value
        self.cursor += 2
        self.input_cursor = 1

    def _OUTPUT(self, mode):
        # print("_OUTPUT", self.cursor)
        self.log("_OUTPUT", self.cursor)
        v1 = self._get_value(self.cursor+1, mode[0])
        self.output.append(v1)
        self.cursor += 2

    def _JUMP_TRUE(self, mode):
        self.log("_JUMP_TRUE", self.cursor)
        v1 = self._get_value(self.cursor + 1, mode[0])
        if v1 != 0:
            self.cursor = self._get_value(self.cursor + 2, mode[1])
        else:
            self.cursor += 3

    def _JUMP_FALSE(self, mode):
        self.log("_JUMP_FALSE", self.cursor)
        self.log("_JUMP_TRUE", self.cursor)
        v1 = self._get_value(self.cursor + 1, mode[0])
        if v1 == 0:
            self.cursor = self._get_value(self.cursor + 2, mode[1])
        else:
            self.cursor += 3

    def _LESS(self, mode):
        self.log("_LESS", self.cursor)
        v1 = self._get_value(self.cursor + 1, mode[0])
        v2 = self._get_value(self.cursor + 2, mode[1])
        self.program[self.program[self.cursor + 3]] = 1 if v1 < v2 else 0
        self.cursor += 4

    def _EQUAL(self, mode):
        self.log("_EQUAL", self.cursor)
        v1 = self._get_value(self.cursor + 1, mode[0])
        v2 = self._get_value(self.cursor + 2, mode[1])
        self.program[self.program[self.cursor + 3]] = 1 if v1 == v2 else 0
        self.cursor += 4

    def _EXIT(self, _):
        self.log("EXIT")
