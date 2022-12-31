import collections

with open ("14/inputs.txt") as f:
    inp = f.readlines()

inp[:] = [line.strip('\n') for line in inp]
start = list(inp.pop(0))

conditions = inp[1:].copy()

conditions[:] = [pair.split(" -> ") for pair in conditions]
pairs = [cond[0] for cond in conditions]
inser = [cond[1] for cond in conditions]

for i in range(40):
    pos = 0
    while pos < len(start) - 1:
        el = start[pos]
        next_el = start[pos + 1]
        if "".join((el, next_el)) in pairs:
            start.insert(pos + 1, inser[pairs.index("".join((el, next_el)))])
            pos += 1
        pos += 1
    print(i)

count = collections.Counter(start)
print(count)




