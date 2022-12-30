depth = 0
forward = 0
aim = 0

with open ("2\inputs.txt") as f:
    moves = f.readlines()

moves[:] = [move.split() for move in moves ]
for move in moves:
    if move[0] == "forward":
        forward += int(move[1][0])
        depth += aim * int(move[1][0])
    elif move[0] == "down":
        aim += int(move[1][0])
    else:
        aim -= int(move[1][0])

print(depth * forward)
