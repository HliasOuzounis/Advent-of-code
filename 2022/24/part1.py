def add(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])


def move_wind(winds, length, height):
    new_winds = []
    for wind in winds:
        new_wind = (add(wind[0], wind[1]), wind[1])
        if new_wind[0][1] > length:
            new_wind = ((wind[0][0], 1), new_wind[1])
        if new_wind[0][1] < 1:
            new_wind = ((wind[0][0], length), new_wind[1])
        if new_wind[0][0] > height:
            new_wind = ((1, wind[0][1]), new_wind[1])
        if new_wind[0][0] < 1:
            new_wind = ((height, wind[0][1]), new_wind[1])
        new_winds.append(new_wind)

    return new_winds


player_moves = ((0, 1), (1, 0), (-1, 0), (0, -1))
# end = (5, 6)
end = (26, 120)
min_moves = 300

cache = {}


def move_player(pos, wind_index, moves, stay, wind_cycle, length, height):
    global min_moves
    if moves + end[0] - pos[0] + end[1] - pos[1] >= min_moves:
        return 999999

    # print(moves, pos, wind_index, min_moves)

    if (pos, wind_index) in cache:
        if cache[(pos, wind_index)] <= moves:
            return 99999

    cache[((pos, wind_index))] = moves

    if (pos, wind_index, moves) in cache:
        return cache[(pos, wind_index, moves)]

    if moves > min_moves:
        return 99999

    total_moves = 99999
    for move in player_moves:
        new_pos = add(move, pos)
        if new_pos == end:
            min_moves = min(min_moves, moves + 1)
            print(min_moves)
            return moves + 1
        if (
            (not 0 < new_pos[1] < length + 1)
            or (not 0 < new_pos[0] < height + 1)
            or new_pos in all_winds[(wind_index + 1) % wind_cycle]
        ):
            continue
        
        total_moves = min(
            total_moves,
            move_player(
                new_pos,
                (wind_index + 1) % wind_cycle,
                moves + 1,
                True,
                wind_cycle,
                length,
                height
            ),
        )
    if stay:
        m = min(wind_cycle - 1, min_moves - moves)
        for i in range(1, m):
            if not pos in all_winds[(wind_index + i) % wind_cycle]:
                total_moves = min(
                    total_moves,
                    move_player(
                        pos, (wind_index + i) % wind_cycle, moves + i, False, wind_cycle, length, height
                    ),
                )

    cache[(pos, wind_index, moves)] = total_moves

    return total_moves


from math import gcd

all_winds = []

import sys
sys.setrecursionlimit(10_000_000)
def main():
    start_wind = []
    for r, line in enumerate(open("input.txt")):
        for c, char in enumerate(line.strip()):
            if char == "^":
                start_wind.append(((r, c), (-1, 0)))
            if char == ">":
                start_wind.append(((r, c), (0, 1)))
            if char == "<":
                start_wind.append(((r, c), (0, -1)))
            if char == "v":
                start_wind.append(((r, c), (1, 0)))

    height = max(wind[0][0] for wind in start_wind)
    length = max(wind[0][1] for wind in start_wind)

    winds = start_wind
    all_winds.append([wind[0] for wind in winds])
    for i in range(1, height * length // gcd(height, length)):
        winds = move_wind(winds, length, height)
        all_winds.append([wind[0] for wind in winds])

        # print(i, "minute")
        # for r in range(7):
        #     for c in range(7):
        #         if (r, c) in all_winds[i]:
        #             print("#", end = "")
        #         else:
        #             print(".", end="")
        #     print()

    wind_cycle = len(all_winds)
    
    start_pos = (0, 1)
    print(move_player(start_pos, 0, 0, True, wind_cycle, length, height))
    print(wind_cycle, length, height)


if __name__ == "__main__":
    main()
