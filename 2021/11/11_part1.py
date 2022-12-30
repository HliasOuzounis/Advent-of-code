
with open ("11/inputs.txt") as f:
    inp = f.readlines()

inp[:] = [[int(octapus) for octapus in line.strip("\n")] for line in inp]

size = len(inp)
s = 0

for i in range(100):
    flashed = []
    for j in range(100):
        for line_n, line in enumerate(inp):
            for pos, octapus in enumerate(line):
                if j == 0: inp[line_n][pos] += 1
                if inp[line_n][pos] > 9 and (line_n, pos) not in flashed:
                    flashed.append((line_n, pos))
                    if line_n > 0:
                        inp[line_n - 1][pos] += 1
                        if pos > 0: inp[line_n - 1][pos - 1] += 1
                        if pos < size - 1: inp[line_n - 1][pos + 1] += 1
                    if line_n < size - 1:
                        inp[line_n + 1][pos] += 1
                        if pos > 0: inp[line_n + 1][pos - 1] += 1
                        if pos < size - 1: inp[line_n + 1][pos + 1] += 1
                    if pos > 0: inp[line_n][pos - 1] += 1
                    if pos < size - 1: inp[line_n][pos + 1] += 1
                
    for line_n, line in enumerate(inp):
        for pos, octapus in enumerate(line):
            if octapus > 9: 
                s += 1
                inp[line_n][pos] = 0
    # print(inp, s)

print(s)


