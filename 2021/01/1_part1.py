larger = 0

with open ("1\inputs.txt") as f:
    depths = f.readlines()
    
depths[:] = [int(d.strip("/n")) for d in depths]

prev = depths[0]
for d in depths[1:]:
    if d > prev:
        larger += 1
    prev = d

print(larger)
    
