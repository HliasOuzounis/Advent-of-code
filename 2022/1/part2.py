def main():
    elves = []
    with open("input.txt") as f:
        lines = f.readlines()
    s = 0
    for line in lines:
        line = line.strip()
        if line.isnumeric():
            s += int(line)
        else:
            elves.append(s)
            s = 0
    sort = sorted(elves, reverse=True)
    print(sort[0] + sort[1] + sort[2])

if __name__ == "__main__":
    main()