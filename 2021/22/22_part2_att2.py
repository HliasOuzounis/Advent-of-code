with open ("inputs.txt") as f:
    inp = f.readlines()

on_off = [line.split(" ")[0] == "on" for line in inp]
inp[:] = [line.strip("\n").replace("on x=", "").replace("off x=", "").replace("y=", "").replace("z=", "").split(",") for line in inp]

inp[:] = [[[int(i) for i in pair.split("..")] for pair in line] for line in inp]


