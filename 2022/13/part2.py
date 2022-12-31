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


def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if not correct_order(arr[j], arr[j + 1]):
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return


def main():
    packages = [[[2]], [[6]]]
    for line in open("input.txt"):
        if len(line.strip()):
            packages.append(parse_line(line))

    bubbleSort(packages)
    print((packages.index([[2]]) + 1) * (packages.index([[6]]) + 1))


if __name__ == "__main__":
    main()
