elves = []
INF = 999999999


def add(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])

elve_rules = [
    lambda x: (-1, 0) if not any(add(x, (-1, i)) in elves for i in (-1, 0, 1)) else None,
    lambda x: (1, 0) if not any(add(x, (1, i)) in elves for i in (-1, 0, 1)) else None,
    lambda x: (0, -1) if not any(add(x, (i, -1)) in elves for i in (-1, 0, 1)) else None, 
    lambda x: (0, 1) if not any(add(x, (i, 1)) in elves for i in (-1, 0, 1)) else None 
]

def alone(elve):
    return not any(
        add(elve, (i, j)) in elves for i in (-1, 0, 1) for j in (-1, 0, 1) if not i == j == 0 
    )


def move_elves(elve_round):
    considered_positions = {}
    for elve in elves:
        if alone(elve):
            considered_positions[elve] = [elve]
            continue
        i = 0
        for i in range(4):
            if (desired_move := elve_rules[(elve_round + i)% 4](elve)) is not None:
                break
        else:
            considered_positions[elve] = [elve]
            continue
        new_pos = add(elve, desired_move)
        if new_pos in considered_positions:
            considered_positions[new_pos].append(elve)
        else:
            considered_positions[new_pos] = [elve]
    new_elves = []
    for pos, elves_want in considered_positions.items():
        if len(elves_want) == 1:
            new_elves.append(pos)
        else:
            new_elves += elves_want
    return new_elves
    
        
        


def main():
    global elves
    for r, line in enumerate(open("input.txt")):
        for c, char in enumerate(line.strip()):
            if char == "#":
                elves.append((r, c))
    
    for elve_round in range(10):
        elves = move_elves(elve_round)

    north_elve = INF
    south_elve = -INF
    west_elve = INF
    east_elve = -INF
    for elve in elves:
        north_elve = min(north_elve, elve[0])
        south_elve = max(south_elve, elve[0])
        west_elve = min(west_elve, elve[1])
        east_elve = max(east_elve, elve[1])

    print((south_elve - north_elve + 1) * (east_elve - west_elve + 1) - len(elves))

    # for i in range(13):
        # for j in range(13):
            # if (i, j) in elves:
                # print("#", end="")
            # else:
                # print(".", end="")
        # print()

if __name__ == "__main__":
    main()