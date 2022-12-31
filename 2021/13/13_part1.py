import collections
with open ("13/inputs.txt") as f:
    inp = f.readlines()

points = [point.strip("\n").split(",") for point in inp if "," in point]
points = [(int(point[0]), int(point[1])) for point in points]
folds = [fold.strip("\n") for fold in inp if "fold" in fold]

size_x = max([int(point[0]) for point in points])
size_y = max([int(point[1]) for point in points])
print(size_x, size_y)

print(folds)
print(len(points))

# for fold in folds:
fold = folds[0]
new_points = []
fold = fold.split("=")
fold_pos = int(fold[1])
if fold[0][-1] == "x":
    for point in points:
        if point[0] > fold_pos:
            new_points.append((size_x - point[0], point[1]))
        else:
            new_points.append(point)

    points = list(set(new_points))

print(len(points))