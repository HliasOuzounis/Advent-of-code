moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def add(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])


def search(matrix, pos):
    return matrix[pos[0]][pos[1]]


def make_move(pos, maze, teleport, move, amount):

    max_row = len(maze)
    max_col = len(maze[0])

    for i in range(amount):
        pos = add(pos, move)
        pos = (pos[0] % max_row, pos[1] % max_col)
        if not (obstacle := search(maze, pos)):
            return (pos[0] - move[0], pos[1] - move[1])
        if obstacle == 2:
            if not pos in teleport:
                teleport_pos = find_teleport_pos(pos, maze, move)
                teleport[(pos, move)] = teleport_pos

            teleport_pos = teleport[(pos, move)]
            if not (obstacle := search(maze, teleport_pos)):
                return (pos[0] - move[0], pos[1] - move[1])
            pos = teleport_pos

    return pos


def find_teleport_pos(pos, maze, move):
    max_row = len(maze)
    max_col = len(maze[0])

    while search(maze, pos) == 2:
        pos = add(pos, move)
        pos = (pos[0] % (max_row - 1), pos[1] % (max_col - 1))
    return pos


def main():
    lines = open("input.txt").readlines()
    movement = lines[-1].strip()

    maze = []
    max_size = 0
    for line in lines[:-2]:
        row = [2]
        for char in line:
            if char == " ":
                row.append(2)
            elif char == ".":
                row.append(1)
            elif char == "#":
                row.append(0)
            else:
                row.append(2)
        max_size = max(max_size, len(row))
        k = max_size - len(row)
        row += [2] * k
        maze.append(row)

    maze = [[2] * len(maze[0])] + maze + [[2] * len(maze[-1])]
    pos = find_teleport_pos((1, 1), maze, (0, 1))

    print(pos)

    teleport = {}
    num = ""
    move_id = 0
    move = moves[0]
    for char in movement.strip():
        if not char in ("R", "L"):
            num += char
            continue
        move_id += 1 if char == "R" else -1

        pos = make_move(pos, maze, teleport, move, int(num))
        print(pos, num, move)
        move = moves[move_id % 4]
        num = ""

    pos = make_move(pos, maze, teleport, move, int(num))
    print(pos[0] * 1000 + pos[1] * 4 + move_id % 4)


if __name__ == "__main__":
    main()
