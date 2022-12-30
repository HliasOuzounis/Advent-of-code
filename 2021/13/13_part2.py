import collections
with open ("13/inputs.txt") as f:
    inp = f.readlines()

points = [point.strip("\n").split(",") for point in inp if "," in point]
points = [(int(point[0]), int(point[1])) for point in points]
folds = [fold.strip("\n") for fold in inp if "fold" in fold]

for fold in folds:

    size_x = max([int(point[0]) for point in points])
    size_y = max([int(point[1]) for point in points])

    new_points = []
    print(fold)
    fold = fold.split("=")
    fold_pos = int(fold[1])
    if fold[0][-1] == "x":
        for point in points:
            if point[0] > fold_pos:
                new_points.append((size_x - point[0], point[1]))
            else:
                new_points.append(point)

    if fold[0][-1] == "y":
        for point in points:
            if point[1] > fold_pos:
                new_points.append((point[0], size_y - point[1]))
            else:
                new_points.append(point)

    points = list(set(new_points))

size_x = max([int(point[0]) for point in points])
size_y = max([int(point[1]) for point in points])
for y in range(size_y + 1):
    for x in range(size_x + 1):
        if (x, y) in points:
            print("*", end= "")
        else: print("-", end="")
    print("")
