wins = {"A": 2 + 6, "B": 3 + 6, "C": 1 + 6}
draw = {"A": 1 + 3, "B": 2 + 3, "C": 3 + 3}
loss = {"A": 3, "B": 1, "C": 2}

choice = {"X": loss, "Y": draw, "Z": wins}


def main():
    with open("input.txt") as f:
        lines = f.readlines()
    lines = list(map(lambda x: x.strip().split(), lines))
    s = 0
    for elf_hand, player_hand in lines:
        s += choice[player_hand][elf_hand]
    print(s)


if __name__ == "__main__":
    main()
