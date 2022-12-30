from copy import deepcopy
import time

with open ("19/inputs.txt") as f:
    inp = f.readlines()
inp[:] = [line.strip("\n") for line in inp]

def to_int(x):
    return int(x)

scanners = []
temp = []
skip_next = True
for line in inp:
    if not line:
        scanners.append(set(tuple(temp.copy())))
        temp = []
        skip_next = True
    elif skip_next: 
        skip_next = False
        continue
    else:
        temp.append(tuple(map(to_int, line.split(","))))

scanner0 = scanners[0]

def rotations(scanner):
    rots = [[] for _ in range(24)]
    for coord in scanner:
        #positive x
        rots[ 0].append((+coord[0],+coord[1],+coord[2]))
        rots[ 1].append((+coord[0],-coord[2],+coord[1]))
        rots[ 2].append((+coord[0],-coord[1],-coord[2]))
        rots[ 3].append((+coord[0],+coord[2],-coord[1]))
        #negative x
        rots[ 4].append((-coord[0],-coord[1],+coord[2]))
        rots[ 5].append((-coord[0],+coord[2],+coord[1]))
        rots[ 6].append((-coord[0],+coord[1],-coord[2]))
        rots[ 7].append((-coord[0],-coord[2],-coord[1]))
        #positive y
        rots[ 8].append((+coord[1],+coord[2],+coord[0]))
        rots[ 9].append((+coord[1],-coord[0],+coord[2]))
        rots[10].append((+coord[1],-coord[2],-coord[0]))
        rots[11].append((+coord[1],+coord[0],-coord[2]))
        #negative y
        rots[12].append((-coord[1],-coord[2],+coord[0]))
        rots[13].append((-coord[1],+coord[0],+coord[2]))
        rots[14].append((-coord[1],+coord[2],-coord[0]))
        rots[15].append((-coord[1],-coord[0],-coord[2]))
        #positive z
        rots[16].append((+coord[2],+coord[0],+coord[1]))
        rots[17].append((+coord[2],-coord[1],+coord[0]))
        rots[18].append((+coord[2],-coord[0],-coord[1]))
        rots[19].append((+coord[2],+coord[1],-coord[0]))
        #negative z
        rots[20].append((-coord[2],-coord[0],+coord[1]))
        rots[21].append((-coord[2],+coord[1],+coord[0]))
        rots[22].append((-coord[2],+coord[0],-coord[1]))
        rots[23].append((-coord[2],-coord[1],-coord[0]))
    return rots

def find_common_beacons(scanner1, scanner2):
    for beacon1 in scanner1:
        for beacon2 in scanner2:
            diff = [pos1 - pos2 for pos1, pos2 in zip(beacon1, beacon2)]
            adjusted_scanner2 = {
                tuple(pos1 + pos2 for pos1, pos2 in zip(beacon, diff))
                for beacon in scanner2
            }

            hits = adjusted_scanner2 & scanner1 # intersection
            if len(hits) >= 12:
                return diff
    return []

def adjust_array(array, diff):
    return tuple(
        tuple(pos1 + pos2 for pos1, pos2 in zip(row, diff)) for row in array
    )

diffs = [(0, 0, 0)]
before_merge_diffs = {}

def merge_scanners():
    merged = False
    for n_scanner1, scanner1 in enumerate(scanners):
        for scanner2 in scanners[n_scanner1+1:]:
            for orientation in rotations(scanner2):
                diff = find_common_beacons(scanner1, orientation)
                if diff:
                    scanner1_copy = tuple(deepcopy(scanner1))
                    scanner1.update(adjust_array(orientation, diff))
                    scanner1_key = tuple(deepcopy(scanner1))
                    scanner2_key = tuple(deepcopy(scanner2))
                    scanners.remove(scanner2)
                    if scanner1 == scanner0:
                        diffs.append(diff)
                        if scanner2_key in before_merge_diffs:
                            for dist in before_merge_diffs[scanner2_key]:
                                diffs.append([pos1 + pos2 for pos1, pos2 in zip(dist, diff)])
                    else:
                        if scanner1_copy in before_merge_diffs:
                            before_merge_diffs[scanner1_key] = [diff]
                            before_merge_diffs[scanner1_key] += before_merge_diffs[scanner1_copy]
                        else:
                            before_merge_diffs[scanner1_key] = [diff]
                        if scanner2_key in before_merge_diffs:
                            for dist in before_merge_diffs[scanner2_key]:
                                before_merge_diffs[scanner1_key].append([pos1 + pos2 for pos1, pos2 in zip(dist, diff)])
                    print(len(scanners), "left")
                    merged = True
        if merged: 
            merge_scanners()
            merged = False
    return

time1 = time.time()
merge_scanners()

distance_max = 0
print(len(diffs))
print(diffs)
for diff1 in diffs:
    for diff2 in diffs:
        if diff1 == diff2: continue
        distance = sum(abs(pos1 - pos2) for pos1, pos2 in zip(diff1, diff2))
        distance_max = max(distance_max, distance)
print(distance_max)
print(time.time() - time1)   