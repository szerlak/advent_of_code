from lib.Intcode import Intcode

with open("data/13.txt") as f:
    _program = list(map(int, f.readline().split(",")))

computer = Intcode(_program, debug=False)


blocks = 0
while computer.is_running:
    computer.run()
    computer.run()
    block_type = computer.run()
    blocks += block_type == 2
print(blocks)


_program[0] = 2
computer = Intcode(_program, debug=False)

ball_x = paddle_x = None
points = 0
input = 0
while computer.is_running:
    x = computer.run(input)
    y = computer.run()
    blocktype = computer.run()
    if computer.is_running:
        paddle_x = x if blocktype == 3 else paddle_x
        ball_x = x if blocktype == 4 else ball_x
        points = blocktype if (x, y) == (-1, 0) else points
    if paddle_x and ball_x:
        input = (ball_x > paddle_x) - (ball_x < paddle_x)
        # print(input)
    # print(ball_x, paddle_x)

print(points)
