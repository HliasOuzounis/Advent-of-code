start = (500, 0)

movement = ((0, 1), (-1, 1), (1, 1))


def sub(tuple1, tuple2):
    return (tuple1[0] - tuple2[0], tuple1[1] - tuple2[1])


def add(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])


class Wall:
    def __init__(self, start, end) -> None:
        self.x0, self.y0 = start
        self.x1, self.y1 = end

    def in_wall(self, point):
        x, y = point
        return (
            abs(self.x0 - x) + abs(self.x1 - x) == abs(self.x0 - self.x1)
        ) and (
            abs(self.y0 - y) + abs(self.y1 - y) == abs(self.y0 - self.y1)
        )


def place_sand(sand_pos, walls, prev_sand, lowest_wall, left_wall, right_wall):
    for move in movement:
        next_pos = add(sand_pos, move)
        if next_pos[1] > lowest_wall or not (left_wall < next_pos[0] < right_wall):
            return False
        if next_pos in prev_sand or any(wall.in_wall(next_pos) for wall in walls):
            continue
        return place_sand(next_pos, walls, prev_sand, lowest_wall, left_wall, right_wall)
    prev_sand.append(sand_pos)
    return True


def main():
    walls = []
    lowest_wall, left_wall, right_wall = 0, 0, 0
    for line in open("input.txt"):
        wall_segments = [
            tuple(map(int, wall.split(","))) for wall in line.strip().split(" -> ")
        ]
        for i in range(len(wall_segments) - 1):
            walls.append(Wall(wall_segments[i], wall_segments[i + 1]))
            lowest_wall = max(lowest_wall, wall_segments[i][1])
            left_wall = min(left_wall, wall_segments[i][0])
            right_wall = max(right_wall, wall_segments[i][0])

    sand = 0
    prev_sand = []
    while place_sand(start, walls, prev_sand, lowest_wall, left_wall, right_wall):
        sand += 1
    print(sand)

if __name__ == "__main__":
    main()
