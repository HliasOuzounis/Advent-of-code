def main():
    crates = [
        [],
        ["C", "F", "B", "L", "D", "P", "Z", "S"],
        ["B", "W", "H", "P", "G", "V", "N"],
        ["G", "J", "B", "W", "F"],
        ["S", "C", "W", "L", "F", "N", "J", "G"],
        ["H", "S", "M", "P", "T", "L", "J", "W"],
        ["S", "F", "G", "W", "C", "B"],
        ["W", "B", "Q", "M", "P", "T", "H"],
        ["T", "W", "S", "F"],
        ["R", "C", "N"]
    ]

    with open("input.txt") as f:
        instructions = [tuple(map(int, line.strip().split())) for line in f]
    
    for n, start, end in instructions:
        moved = crates[start][-n:]
        crates[start] = crates[start][:-n]
        crates[end] += moved[::-1]       
    
    print("".join(crate[-1] for crate in crates if crate))

if __name__ == "__main__":
    main()