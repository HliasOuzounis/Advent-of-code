def calculate_value(monkey):
    op = monkey_tree[monkey]
    if len(op) == 1:
        return int(op[0])

    monkey1, op, monkey2 = op

    if op == "+":
        return calculate_value(monkey1) + calculate_value(monkey2)
    elif op == "-":
        return calculate_value(monkey1) - calculate_value(monkey2)
    elif op == "*":
        return calculate_value(monkey1) * calculate_value(monkey2)
    elif op == "/":
        return calculate_value(monkey1) / calculate_value(monkey2)

    return 0


monkey_tree = {}


def main():

    for line in open("input.txt"):
        name, operation = line.strip().split(": ")
        operation = operation.split()
        monkey_tree[name] = operation

    print(int(calculate_value("root")))


if __name__ == "__main__":
    main()
