moves = {"D": (1, 0), "U": (-1, 0), "L": (0, -1), "R": (0, 1)}
diag_moves = {"DL": (1, -1), "DR": (1, 1), "UL": (-1, -1), "UR": (-1, 1)}

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

    snake = [(0, 0) for _nodes in range(10)]
    visited_positions = {(0, 0)}
    
    for command in commands:
        move, n = command.split()
        move = moves[move]
        n = int(n.strip())

        for i in range(n):
            head = (snake[0][0] + move[0], snake[0][1] + move[1])
            snake[0] = head

            for i in range(1, len(snake)):
                head = snake[i - 1]
                tail = snake[i]
                if not is_near(tail, head):
                    if not head[0] == tail[0] and not head[1] == tail[1]:
                        for sub_move in diag_moves.values():
                            if is_near((tail[0] + sub_move[0], tail[1] + sub_move[1]), head):
                                snake[i] = (tail[0] + sub_move[0], tail[1] + sub_move[1])
                                break
                    else:
                        for sub_move in moves.values():
                            if is_near((tail[0] + sub_move[0], tail[1] + sub_move[1]), head):
                                snake[i] = (tail[0] + sub_move[0], tail[1] + sub_move[1])
                                break
            visited_positions.add(snake[-1])


    print(len(visited_positions))


if __name__ == "__main__":
    main()
