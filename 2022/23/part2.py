elves = []
INF = 999999999


def add(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])


elve_rules = [
    lambda x: (-1, 0)
    if not any(add(x, (-1, i)) in elves for i in (-1, 0, 1))
    else None,
    lambda x: (1, 0) if not any(add(x, (1, i)) in elves for i in (-1, 0, 1)) else None,
    lambda x: (0, -1)
    if not any(add(x, (i, -1)) in elves for i in (-1, 0, 1))
    else None,
    lambda x: (0, 1) if not any(add(x, (i, 1)) in elves for i in (-1, 0, 1)) else None,
]


def alone(elve):
    return not any(
        add(elve, (i, j)) in elves
        for i in (-1, 0, 1)
        for j in (-1, 0, 1)
        if not i == j == 0
    )


def move_elves(elve_round):
    considered_positions = {}
    new_elves = []
    moved = False
    for elve in elves:
        if alone(elve):
            new_elves.append(elve)
            continue
        i = 0
        for i in range(4):
            if (desired_move := elve_rules[(elve_round + i) % 4](elve)) is not None:
                break
        else:
            considered_positions[elve] = [elve]
            continue
        new_pos = add(elve, desired_move)
        moved = True
        if new_pos in considered_positions:
            considered_positions[new_pos].append(elve)
        else:
            considered_positions[new_pos] = [elve]

    for pos, elves_want in considered_positions.items():
        if len(elves_want) == 1:
            new_elves.append(pos)
        else:
            new_elves += elves_want

    return new_elves, moved


def main():
    global elves
    for r, line in enumerate(open("input.txt")):
        for c, char in enumerate(line.strip()):
            if char == "#":
                elves.append((r, c))
    elve_round = 0
    while 1:
        elves, moved = move_elves(elve_round)
        elve_round += 1
        print(elve_round)
        if not moved:
            break

    # for i in range(13):
    # for j in range(13):
    # if (i, j) in elves:
    # print("#", end="")
    # else:
    # print(".", end="")
    # print()


if __name__ == "__main__":
    main()
