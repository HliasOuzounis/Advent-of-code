wins = {"A": "Y", "B": "Z", "C": "X"}
draw = {"A": "X", "B": "Y", "C": "Z"}
score = {"Y": 2, "X": 1, "Z": 3}

def main():
    with open("input.txt") as f:
        lines = f.readlines()
    lines = list(map(lambda x: x.strip().split(), lines))
    s = 0
    for elf_hand, player_hand in lines:
        s += score[player_hand]
        if player_hand == wins[elf_hand]:
            s += 6
        elif player_hand == draw[elf_hand]:
            s += 3
    print(s)




if __name__ == "__main__":
    main()