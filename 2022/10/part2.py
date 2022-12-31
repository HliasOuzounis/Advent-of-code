cutoff = 40
def next_cycle(cycle):
    return (cycle + 1) % cutoff

def main():
    with open("input.txt") as f:
        ops = f.readlines()

    cycle = 0
    sprite_pos = (0, 1, 2)

    render = ""

    for command in ops:
        
        if "noop" in command:
            render += "#" if cycle in sprite_pos else "."
            cycle = next_cycle(cycle)
            continue
        
        render += "#" if cycle in sprite_pos else "."
        cycle = next_cycle(cycle)
        render += "#" if cycle in sprite_pos else "."
        cycle = next_cycle(cycle)
        
        add = int(command.split()[1])
        sprite_pos = tuple(map(lambda x: x + add, sprite_pos))
    
    
    for pos, sprite in enumerate(render):
        print(sprite, end="")
        if (pos + 1) % cutoff == 0:
            print()

if __name__ == "__main__":
    main()