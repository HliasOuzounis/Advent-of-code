with open ("inputs.txt") as f:
    inp = f.readlines()

on_off = [line.split(" ")[0] == "on" for line in inp]
inp[:] = [line.strip("\n").replace("on x=", "").replace("off x=", "").replace("y=", "").replace("z=", "").split(",") for line in inp]

inp[:] = [[[int(i) for i in pair.split("..")] for pair in line] for line in inp]

table = [[[False for x in range(101)] for y in range(101)] for z in range (101)]

for (x, y, z), toggle in zip(inp, on_off):
    x_start, x_end = x
    y_start, y_end = y
    z_start, z_end = z

    if x_start < -50 or x_start > 50: break

    for _x in range(x_start, x_end + 1):
        for _y in range(y_start, y_end + 1):
            for _z in range(z_start, z_end + 1):
                if toggle:
                    table[_x + 50][_y + 50][_z + 50] = True
                else: 
                    table[_x + 50][_y + 50][_z + 50] = False
count = 0
for x in table:
    for y in x:
        for z in y:
            if z: count += 1

print(count) 
    
