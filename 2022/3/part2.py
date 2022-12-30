def main():
    with open("input.txt") as f:
        crates = f.readlines()
    
    matches = []
    for group1, group2, group3 in zip(crates[::3], crates[1::3], crates[2::3]):
        for j in group1:
            if j in group2 and j in group3:
                matches.append(j)
                break
    print(sum(ord(match) - 64 + 26 if match.isupper() else ord(match) - 96 for match in matches))


if __name__ == "__main__":
    main()