def is_adj(cube1, cube2):
    if sum((cube1[i] == cube2[i]) for i in (0, 1, 2)) == 2:
        return any(cube1[i] in (cube2[i] - 1, cube2[i] + 1) for i in (0, 1, 2))
    return False


move = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def inside(air_cube, cubes):
    is_inside = True
    queue = [air_cube]
    visited = []
    while queue:
        cube = queue.pop(0)
        if any(0 > k or k >= 20 for k in cube):
            is_inside = False
            continue

        if cube in visited or cube in cubes:
            continue

        visited.append(cube)

        for (x, y, z) in move:
            next_cube = (cube[0] + x, cube[1] + y, cube[2] + z)
            if not next_cube in visited:
                queue.append(next_cube)

    return visited, is_inside


def calculate_area(cubes):
    if not cubes:
        return 0

    sides = 0
    checked = []
    for cube in cubes:
        sides += 6
        for cube2 in checked:
            if is_adj(cube, cube2):
                sides -= 2
        checked.append(cube)

    return sides


def main():
    cubes = [tuple(map(int, line.split(","))) for line in open("input.txt")]

    air_cubes = []
    for x in range(21):
        for y in range(21):
            for z in range(21):
                air_cube = (x, y, z)
                if not air_cube in cubes:
                    air_cubes.append(air_cube)

    trapped_air = []
    while air_cubes:
        air_cube = air_cubes.pop()
        visited, is_inside = inside(air_cube, cubes)
        if is_inside:
            trapped_air += visited
        air_cubes[:] = [air for air in air_cubes if air not in visited]

    print(calculate_area(cubes) - calculate_area(trapped_air))


if __name__ == "__main__":
    main()
