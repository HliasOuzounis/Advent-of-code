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
        
    def split_cubes(self, other_cube):
        # Check if they intersect
        if self.x[1] < other_cube.x[0]: return [self, other_cube]
        if self.x[0] > other_cube.x[1]: return [self, other_cube]

        if self.y[1] < other_cube.y[0]: return [self, other_cube]
        if self.y[0] > other_cube.y[1]: return [self, other_cube]
        
        if self.z[1] < other_cube.z[0]: return [self, other_cube]
        if self.z[0] > other_cube.z[1]: return [self, other_cube]

        indexes = [0, 1]
        points_in_cube = []
        for x_index, y_index, z_index in itertools.product(indexes, repeat=3):
            point = (other_cube.x[x_index], other_cube.y[y_index], other_cube.z[z_index])
            if self.point_is_in_cube(point):
                points_in_cube.append(point)
        if len(points_in_cube) == 8: 
            if self.toggle == other_cube.toggle: return [self]
            else:
                new_cubes = []
                for x_index, y_index, z_index in itertools.product(indexes, repeat=3):
                    new_cubes.append(Cube(
                                            (self.x[x_index], other_cube.x[x_index]),
                                            (self.y[y_index], other_cube.y[y_index]),
                                            (self.z[z_index], other_cube.z[z_index]),
                                            self.toggle
                                            )) 
                z_index = 1
                for x_index, y_index in itertools.product([0,1], repeat=2):
                    new_cubes.append(Cube(
                                            (self.x[not x_index], other_cube.x[x_index]),
                                            (self.y[y_index], other_cube.y[y_index]),
                                            (self.z[z_index], other_cube.z[z_index]),
                                            self.toggle
                                            )) 

    def point_is_in_cube(self, point):

        if self.x[0] > point[0]: return False
        if self.x[1] < point[0]: return False
        
        if self.y[0] > point[1]: return False
        if self.y[1] < point[1]: return False
        
        if self.z[0] > point[2]: return False
        if self.z[1] < point[2]: return False

        return True

    def get_volume(self):
        return (self.x[1] - self.x[0]) * (self.y[1] - self.y[0]) * (self.z[1] - self.z[0])

def split_cubes(cube1, cube2):
    intersection = cube1.get_intersection(cube2)
    if intersection:
        return # [cubes]
    return [cube1, cube2]

on_cubes = []
off_cubes = []
for toggle, (x, y, z) in zip(on_off, inp):
    if toggle:
        on_cubes.append(Cube(x, y, z, toggle))
    else:
        off_cubes.append(Cube(x, y, z, toggle))

lit_cubes = sum([on_cube.get_volume() for on_cube in on_cubes]) - sum(off_cube.get_volume() for off_cube in off_cubes)

print(lit_cubes)