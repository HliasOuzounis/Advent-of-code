
with open ("14/inputs.txt") as f:
    inp = f.readlines()

inp[:] = [line.strip('\n') for line in inp]
start = inp.pop(0)

conditions = inp[1:].copy()

conditions[:] = [pair.split(" -> ") for pair in conditions]
pairs = [cond[0] for cond in conditions]
inser = {condition[0]: condition[1] for condition in conditions}

start_dict_m = {condition[0]: 0 for condition in conditions}

start_dict = start_dict_m.copy()
for pos in range(len(start) - 1):
    print(start[pos:pos + 2])
    start_dict[start[pos : pos + 2]] += 1
print(start_dict)

for i in range(40):
    d = start_dict_m.copy()
    for pair, count in start_dict.items():
        new_ch = inser[pair]
        d["".join((pair[0], new_ch))] += count
        d["".join((new_ch, pair[1]))] += count
    start_dict = d.copy()
    print(i)

d = {cond[1]: 0 for cond in conditions}
print(d)
for pair, count in start_dict.items():
    d[pair[0]] += count
    d[pair[1]] += count


res = sorted(d.items(), key = lambda x: x[1], reverse = True)
print(res)
print((res[0][1] - res[-1][1])/2)
