with open ("1\inputs.txt") as f:
    depths = f.readlines()
    
depths[:] = [int(d.strip("/n")) for d in depths]

depth_sums = [depths[i] + depths[i + 1] + depths[i + 2] for i, d in enumerate(depths[:-2])]
larger = 0

prev = depth_sums[0]
for d in depth_sums[1:]:
    if d > prev:
        larger += 1
    prev = d

print(larger)
