def main():
    pairs = []
    with open("input.txt") as f:
        for line in f:
            pair1, pair2 = line.split(",")
            pairs.append(
                (tuple(map(int, pair1.split("-"))), tuple(map(int, pair2.split("-"))))
            )
    ans = 0
    for pair1, pair2 in pairs:
        if pair1[0] <= pair2[0] <= pair1[1] or pair1[0] <= pair2[1] <= pair1[1]:
            ans += 1
        elif pair2[0] <= pair1[0] <= pair2[1] or pair2[0] <= pair1[1] <= pair2[1]:
            ans += 1

    print(ans)

if __name__ == "__main__":
    main()
