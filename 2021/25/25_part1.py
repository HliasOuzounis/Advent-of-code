
with open("input.txt") as f:
    inp = [line.strip() for line in f.readlines()]

h = len(inp)
w = len(inp[0])
print(h, w)

i = 2
j = 4

moved = True
east_facing = True

steps = 0
while moved or not east_facing:
    steps += 1 if east_facing else 0
    moved = False if east_facing else moved
    inp_copy = inp.copy()
    for i, line in enumerate(inp_copy):
        for j, cucamber in enumerate(line):
            if cucamber == ".": continue
            if east_facing:
                if cucamber == "v": continue
                if j < w - 1:
                    if line[j+1] != ".": continue
                    else: 
                        moved = True
                        inp[i] = inp[i][:j] + ".>" + inp[i][j+2:]
                else:
                    if inp_copy[i][0] != ".": continue
                    else: 
                        moved = True
                        inp[i] = ">" + inp[i][1:w-1] + "."
            else:
                if cucamber == ">": continue
                if i < h - 1:
                    # print(j, i)
                    if inp[i+1][j] != ".": continue
                    else:
                        moved = True
                        inp[i] = inp[i][:j] + "." + inp[i][j+1:]
                        inp[i+1] = inp[i+1][:j] + "v" + inp[i+1][j+1:]
                else:
                    if inp_copy[0][j] != ".": continue
                    else:
                        moved = True
                        inp[-1] = inp[-1][:j] + "." + inp[-1][j+1:]
                        inp[0] = inp[0][:j] + "v" + inp[0][j+1:]
            
    east_facing = not east_facing
    if east_facing:
        # for line in inp:
        #     print(line)
        print("next step", steps)
print(steps)