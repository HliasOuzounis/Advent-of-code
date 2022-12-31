def main():
    with open("input.txt") as f:
        crates = f.readlines()
    halves = []
    for crate in crates:
        l = len(crate)
        halves.append((crate[: l // 2], crate[l // 2 :].strip()))

    matches = []
    for halve1, halve2 in halves:
        for j in halve1:
            if j in halve2:
                matches.append(j)
                break
            
    print(sum(ord(match) - 64 + 26 if match.isupper() else ord(match) - 96 for match in matches))


if __name__ == "__main__":
    main()
