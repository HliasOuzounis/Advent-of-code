from copy import deepcopy

parsed_line = None

def parse_line(line):
    exec("global parsed_line; parsed_line = " + line)
    return deepcopy(parsed_line)


def correct_order(l1, l2):
    if isinstance(l1, int) and isinstance(l2, int):
        return l2 - l1
        
    if isinstance(l2, int):
        l2 = [l2]
    if isinstance(l1, int):
        l1 = [l1]

    k = min(len(l1), len(l2))
    for i in range(k):
        if not (res := correct_order(l1[i], l2[i])) is 0:
            return res > 0

    return len(l1) < len(l2)


def main():
    index = 1
    ans = 0

    first = 0
    compare = [[], []]
    for line in open("input.txt"):
        if len(line.strip()) == 0:
            if s := correct_order(compare[0], compare[1]):
                ans += index
            index += 1
        else:
            compare[first] = parse_line(line)
            first = not first

    if s:= correct_order(compare[0], compare[1]):
        ans += index

    print(ans)

if __name__ == "__main__":
    main()
