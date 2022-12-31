def main():
    trees = []
    with open("input.txt") as f:
        for line in f:
            trees.append([int(tree) for tree in line.strip()])

    max_scenery = 0

    for tree_i in range(1, len(trees) - 1):
        for tree_j in range(1, len(trees) - 1):
            tree_size = trees[tree_i][tree_j]
            scenery = 1
            for direction in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                i, j = tree_i, tree_j
                direction_scenery = 0
                while 0 < i < len(trees) - 1 and 0 < j < len(trees[0]) - 1:
                    i += direction[0]
                    j += direction[1]
                    if trees[i][j] < tree_size:
                        direction_scenery += 1
                    else:
                        direction_scenery += 1
                        break
                scenery *= direction_scenery
                
            max_scenery = max(max_scenery, scenery)
    print(max_scenery)


if __name__ == "__main__":
    main()
