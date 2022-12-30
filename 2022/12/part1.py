moves = ((1, 0), (-1, 0), (0, 1), (0, -1))


def is_out(pos, rows, cols):
    return not (0 <= pos[0] < rows and 0 <= pos[1] < cols)


def bfs(table, start_pos, end_pos):
    queue = [(start_pos, 0)]
    visited = []

    while queue:
        pos, distance = queue.pop(0)
        if pos in visited:
            continue
        visited.append(pos)
        if pos == end_pos:
            return distance

        for move in moves:
            neighbour = (pos[0] + move[0], pos[1] + move[1])
            if is_out(neighbour, len(table), len(table[0])):
                continue
            if table[neighbour[0]][neighbour[1]] <= table[pos[0]][pos[1]] + 1:
                queue.append((neighbour, distance + 1))

    return "Not found"


def main():
    with open("input.txt") as f:
        table = [[elevation for elevation in line.strip()] for line in f.readlines()]
    for i, row in enumerate(table):
        for j, elevation in enumerate(row):
            if elevation == "S":
                table[i][j] = 0
                start_pos = (i, j)
            elif elevation == "E":
                table[i][j] = 26
                end_pos = (i, j)
            else:
                table[i][j] = ord(elevation) - 97

    min_distance = bfs(table, start_pos, end_pos) - 2
    print(min_distance)


if __name__ == "__main__":
    main()
