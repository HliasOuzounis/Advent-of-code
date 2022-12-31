moves = {"D": (1, 0), "U": (-1, 0), "L": (0, -1), "R": (0, 1)}


def is_near(tail, head):
    return head in (
        (tail[0] + 1, tail[1] + 1),
        (tail[0] + 1, tail[1] - 1),
        (tail[0] + 1, tail[1]),
        (tail[0], tail[1] + 1),
        (tail[0], tail[1] - 1),
        (tail[0], tail[1]),
        (tail[0] - 1, tail[1] + 1),
        (tail[0] - 1, tail[1] - 1),
        (tail[0] - 1, tail[1]),
    )


def main():
    with open("input.txt") as f:
        commands = f.readlines()

    head_pos = (0, 0)
    tail_pos = (0, 0)
    visited_positions = {tail_pos: 1}

    for command in commands:
        move, n = command.split()
        move = moves[move]
        n = int(n.strip())

        for i in range(n):
            head_pos = (head_pos[0] + move[0], head_pos[1] + move[1])
            if not is_near(tail_pos, head_pos):
                tail_pos = (head_pos[0] - move[0], head_pos[1] - move[1])
                visited_positions[tail_pos] = (
                    visited_positions.get(tail_pos, 0) + 1
                )
    print(len(visited_positions))

if __name__ == "__main__":
    main()
