def main():
    trees = []
    with open("input.txt") as f:
        for line in f:
            trees.append([int(tree) for tree in line.strip()])
    ans = 2 * len(trees) + 2 * (len(trees[0]) - 2)

    for i in range(1, len(trees) - 1):
        for j in range(1, len(trees) - 1):
            tree_size = trees[i][j]
            if (
                all(trees[i][k] < tree_size for k in range(j - 1, -1, -1))
                or all(trees[i][k] < tree_size for k in range(j + 1, len(trees[0])))
                or all(trees[k][j] < tree_size for k in range(i - 1, -1, -1))
                or all(trees[k][j] < tree_size for k in range(i + 1, len(trees[0])))
            ):
                ans += 1
    print(ans)

if __name__ == "__main__":
    main()
