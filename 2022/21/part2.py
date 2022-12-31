inv_op = {"+": "-", "-": "+", "*": "/", "/": "*"}

def calculate_value(monkey, target_value = None):
    if monkey == "root":
        monkey1, monkey2 = monkey_tree["root"][::2]
        if monkey1 in important_monkeys:
            return calculate_value(monkey1, calculate_value(monkey2, target_value))
        if monkey2 in important_monkeys:
            return calculate_value(monkey2, calculate_value(monkey1, target_value))
    
    if monkey == "humn":
        return target_value
    
    if len(monkey_tree[monkey]) == 1:
        return int(monkey_tree[monkey][0])

    monkey1, monkey2 = monkey_tree[monkey][::2]
    op = monkey_tree[monkey][1]
    
    if target_value is None:
        if op == "+":
            return calculate_value(monkey1) + calculate_value(monkey2)
        elif op == "-":
            return calculate_value(monkey1) - calculate_value(monkey2)
        elif op == "*":
            return calculate_value(monkey1) * calculate_value(monkey2)
        elif op == "/":
            return calculate_value(monkey1) / calculate_value(monkey2)

    if monkey1 in important_monkeys:
        if op == "+":
            return calculate_value(monkey1, target_value - calculate_value(monkey2))
        elif op == "-":
            return calculate_value(monkey1, target_value + calculate_value(monkey2))
        elif op == "*":
            return calculate_value(monkey1, target_value / calculate_value(monkey2))
        elif op == "/":
            return calculate_value(monkey1, target_value * calculate_value(monkey2))
    else:
        if op == "+":
            return calculate_value(monkey2, target_value - calculate_value(monkey1))
        elif op == "-":
            return calculate_value(monkey2, calculate_value(monkey1) - target_value)
        elif op == "*":
            return calculate_value(monkey2, target_value / calculate_value(monkey1))
        elif op == "/":
            return calculate_value(monkey2, calculate_value(monkey1) / target_value)



monkey_tree = {}
important_monkeys = ["humn"]


def main():

    for line in open("input.txt"):
        name, operation = line.strip().split(": ")
        operation = operation.split()
        monkey_tree[name] = operation

    while "root" not in important_monkeys:
        for monkey in monkey_tree:
            if any(
                important_monkey in monkey_tree[monkey]
                for important_monkey in important_monkeys
            ):
                if monkey not in important_monkeys:
                    important_monkeys.append(monkey)

    print(int(calculate_value("root")))


if __name__ == "__main__":
    main()
