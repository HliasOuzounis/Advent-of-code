with open ("12/inputs.txt") as f:
    inp = f.readlines()

inp[:] = [line.strip("\n").split("-") for line in inp]

d_of_points = {}

for pair in inp:
    for point in pair:
        if not point in d_of_points:
            d_of_points[point] = []

for pair in inp:
    if pair[0] != "end" and pair[1] != "start": d_of_points[pair[0]].append(pair[1])
    if pair[1] != "end" and pair[0] != "start": d_of_points[pair[1]].append(pair[0])

def find_paths(p, visited, visited_small_cave):
    if p == "end":
        return 1

    if p.islower(): visited.append(p)
    nof_paths = 0
    for point in d_of_points[p]:
        if point in visited:
            if visited_small_cave: continue
            else: nof_paths += find_paths(point, visited.copy(), True)
        else:
            nof_paths += find_paths(point, visited.copy(), visited_small_cave)

    return nof_paths

print(find_paths("start", [], False))
    
