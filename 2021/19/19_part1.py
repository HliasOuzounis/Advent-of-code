import itertools
import numpy as np

with open ("19/inputs.txt") as f:
    inp = f.readlines()
inp[:] = [line.strip("\n") for line in inp]

def to_int(x):
    return int(x)

def get_all_orientations(beacons_list):
    orientations = [[] for i in range(24)]
    count = 0
    for negx, negy, negz in itertools.product([-1, 1], repeat = 3):
        for x, y, z in beacons_list:
            orientations[count].append((x * negx, y * negy, z * negz))
            orientations[count + 1].append((y * negx, z * negy, x * negz))
            orientations[count + 2].append((z * negx, x * negy, y * negz))
        count += 3
    return orientations

def check_common_beacons(scanner1, scanner2):
    for beacon1 in scanner1:
        for beacon2 in scanner2:
            diff = [pos1 - pos2 for pos1, pos2 in zip(beacon1, beacon2)]
            # if any([pos > 1000 for pos in diff]): continue
            adjusted_scanner2 = [[pos1 + pos2 for pos1, pos2 in zip(beacon, diff)] for beacon in scanner2]
            hits = [tuple(adj_beacon) for adj_beacon in adjusted_scanner2 if tuple(adj_beacon) in scanner1]
            if len(hits) >= 12:
                print("hits:",hits)
                return diff
    return []

scanners = []
temp = []
skip_next = True
for line in inp:
    if not line:
        scanners.append(tuple(temp.copy()))
        temp = []
        skip_next = True
    elif skip_next: 
        skip_next = False
        continue
    else:
        temp.append(tuple(map(to_int, line.split(","))))

adjusted_scanners = {scanners[0]: (scanners[0], [0, 0, 0])}
all_orientations = [[scanners[0]]]
for scanner in scanners[1:]:
    all_orientations.append(get_all_orientations(scanner))

iter_scanners_list = [(scanners[0], [0, 0, 0])]

for n_scanner1, scanner1 in enumerate(iter_scanners_list):
    for n_scanner2, scanner2 in enumerate(scanners[n_scanner1 + 1:]):
        if scanner2 in iter_scanners_list: continue
        for n_orientation2, orientation2 in enumerate(all_orientations[n_scanner2 + n_scanner1 + 1]):
            diff = check_common_beacons(scanner1[0], orientation2)
            if diff:
                print("Match: scanner {0} with scanner {1} orientation {2}"
                .format(n_scanner1, n_scanner2 + n_scanner1 + 1, n_orientation2))
                diff = np.add(diff, scanner1[1])
                adjusted_scanners[scanner2] = [orientation2, diff]
                print("saved:", orientation2, diff, scanner1[0])
                if not any([orientation in iter_scanners_list for orientation in all_orientations[n_scanner2 + n_scanner1 + 1]]):
                    iter_scanners_list.append((orientation2, diff))
                # scanners.remove(scanner2)
                break
    print("next scanner")

def adjust_table(table, diff):
    return [[pos1 - pos2 for pos1, pos2 in zip(item, diff)] for item in table]

beacons = set([])
for modifiers in adjusted_scanners.values():
    for beacon in adjust_table(modifiers[0], modifiers[1]):
        beacons.add(tuple(beacon))

beacons = sorted(list(beacons), key = lambda x: x[0])
print(len(beacons))
print(beacons)