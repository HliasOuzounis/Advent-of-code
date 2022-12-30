def main():
    with open("input.txt") as f:
        ops = f.readlines()
    
    signal_strenth = 0
    important_cycles = [20, 60, 100, 140, 180, 220]

    cycle = 0
    reigister = 1

    for op in ops:
        op = op.strip()
        if op == "noop":
            cycle += 1
            if cycle in important_cycles:
                signal_strenth += cycle * reigister
                print(signal_strenth, cycle, reigister)
            continue
        add = int(op.split()[1])
        cycle += 1
        if cycle in important_cycles:
            signal_strenth += cycle * reigister
            print(signal_strenth, cycle, reigister)
        cycle += 1
        if cycle in important_cycles:
            signal_strenth += cycle * reigister
            print(signal_strenth, cycle, reigister)
        reigister += add

    print(signal_strenth)

if __name__ == "__main__":
    main()