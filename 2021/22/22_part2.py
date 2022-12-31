import itertools

with open ("inputs.txt") as f:
    inp = f.readlines()

on_off = [line.split(" ")[0] == "on" for line in inp]
inp[:] = [line.strip("\n").replace("on x=", "").replace("off x=", "").replace("y=", "").replace("z=", "").split(",") for line in inp]

inp[:] = [[[int(i) for i in pair.split("..")] for pair in line] for line in inp]

class Cube:
    def __init__(self, x, y, z, toggle) -> None:
        self.x = sorted(x)
        self.y = sorted(y)
        self.z = sorted(z)
        self.toggle = toggle
        
    def get_intersection(self, other_cube):
        # Check if they intersect
        if self.x[1] < other_cube.x[0]: return None
        if self.x[0] > other_cube.x[1]: return None

        if self.y[1] < other_cube.y[0]: return None
        if self.y[0] > other_cube.y[1]: return None
        
        if self.z[1] < other_cube.z[0]: return None
        if self.z[0] > other_cube.z[1]: return None

        toggle = self.toggle or other_cube.toggle
        for x_index, y_index, z_index in itertools.product((0, 1), repeat=3):
            point = (other_cube.x[x_index], other_cube.y[y_index], other_cube.z[z_index])
            if self.point_is_in_cube(point):
                return Cube(
                    (point[0], self.x[not x_index]),
                    (point[1], self.y[not y_index]),
                    (point[2], self.z[not z_index]),
                    toggle
                    )
    
    def point_is_in_cube(self, point):

        if self.x[0] > point[0]: return False
        if self.x[1] < point[0]: return False
        
        if self.y[0] > point[1]: return False
        if self.y[1] < point[1]: return False
        
        if self.z[0] > point[2]: return False
        if self.z[1] < point[2]: return False

        return True

    def volume(self):
        return (self.x[1] - self.x[0]) * (self.y[1] - self.y[0]) * (self.z[1] - self.z[0])

on_cubes = []
off_cubes = []
for toggle, (x, y, z) in zip(on_off, inp):
    if toggle:
        on_cubes.append(Cube(x, y, z, toggle))
    else:
        off_cubes.append(Cube(x, y, z, toggle))

for off_cube in off_cubes.copy():
    for on_cube in on_cubes:
        intersection = off_cube.get_intersection(on_cube)
        if intersection:
            off_cubes.append(intersection)
    off_cubes.remove(off_cube)

for n_cube, cube1 in enumerate(on_cubes):
    for cube2 in on_cubes[n_cube + 1:]:
        intersection = cube1.get_intersection(cube2)
        if intersection:
            off_cubes.append(intersection)

for n_cube, cube1 in enumerate(off_cubes):
    for cube2 in off_cubes[n_cube + 1:]:
        intersection = cube1.get_intersection(cube2)
        if intersection:
            on_cubes.append(intersection)

print(len(on_cubes), len(off_cubes))
lit_cubes = sum([on_cube.volume() for on_cube in on_cubes]) - sum(off_cube.volume() for off_cube in off_cubes)
        
print(lit_cubes, "vs 590784")


    
