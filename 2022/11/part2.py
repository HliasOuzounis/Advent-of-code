class Monkey:
    def __init__(self, start_items, operation, test, test_success, test_fail) -> None:
        self.items = start_items
        self.operation = operation
        self.test = test
        self.success = test_success
        self.fail = test_fail

        self.inspect_count = 0



def main():
    common_mod = 9_699_690
    monkeys = [
        Monkey([91, 66],                         lambda old: (old * 13)  % common_mod,   lambda item: item % 19 == 0, 6, 2),
        Monkey([78, 97, 59],                     lambda old: (old + 7)   % common_mod,   lambda item: item %  5 == 0, 0, 3),
        Monkey([57, 59, 97, 84, 72, 83, 56, 76], lambda old: (old + 6)   % common_mod,   lambda item: item % 11 == 0, 5, 7),
        Monkey([81, 78, 70, 58, 84],             lambda old: (old + 5)   % common_mod,   lambda item: item % 17 == 0, 6, 0),
        Monkey([60],                             lambda old: (old + 8)   % common_mod,   lambda item: item %  7 == 0, 1, 3),
        Monkey([57, 69, 63, 75, 62, 77, 72],     lambda old: (old * 5)   % common_mod,   lambda item: item % 13 == 0, 7, 4),
        Monkey([73, 66, 86, 79, 98, 87],         lambda old: (old * old) % common_mod,   lambda item: item %  3 == 0, 5, 2),
        Monkey([95, 89, 63, 67],                 lambda old: (old + 2)   % common_mod,   lambda item: item %  2 == 0, 1, 4),
    ]
    
    rounds = 10_000
    for _round in range(rounds):
        for monkey in monkeys:
            monkey.items = list(map(monkey.operation, monkey.items))
            monkey.inspect_count += len(monkey.items)
            while monkey.items:
                item = monkey.items.pop(0)
                if monkey.test(item):
                    monkeys[monkey.success].items.append(item)
                else:
                    monkeys[monkey.fail].items.append(item)

    inspection_counts = sorted([monkey.inspect_count for monkey in monkeys], reverse=True)

    print(inspection_counts[0] * inspection_counts[1])


if __name__ == "__main__":
    main()