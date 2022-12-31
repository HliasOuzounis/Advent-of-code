def is_adj(cube1, cube2):
    if sum((cube1[i] == cube2[i]) for i in (0, 1, 2)) == 2:
        return any(
            cube1[i] in (cube2[i] - 1, cube2[i] + 1) for i in (0, 1, 2)
        )
    return False

def main():
    cubes = [tuple(map(int, line.split(","))) for line in open("input.txt")]
    sides = 0
    checked = []
    for cube in cubes:
        sides += 6
        for cube2 in checked:
            if is_adj(cube, cube2):
                sides -= 2
        checked.append(cube)
    print(sides)

if __name__ == "__main__":
    main()