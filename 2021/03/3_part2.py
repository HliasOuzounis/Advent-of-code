with open ("3\inputs.txt") as f:
    report = f.readlines()

report[:] = [str(bits)[:-1] for bits in report]
bit_len = len(str(report[0]))
report[-1] = "110011100110"

for bits in report:
    if len(bits) != bit_len:
        print(bits)

co2_candidates = report.copy()
i = 0
while len(co2_candidates) != 1:
    bit_count = 0
    for bits in co2_candidates:
        bit_count += int(bits[i])
    mcb = 1-bit_count/len(co2_candidates)
    co2_candidates[:] = [bits for bits in co2_candidates if int(bits[i]) == round(mcb)]
    i += 1

oxygen_candidates = report.copy()
i = 0
while len(oxygen_candidates) != 1:
    bit_count = 0
    for bits in oxygen_candidates:
        bit_count += int(bits[i])
    mcb = bit_count/len(oxygen_candidates) + 0.0001
    oxygen_candidates[:] = [bits for bits in oxygen_candidates if int(bits[i]) == round(mcb)]
    i += 1

print(oxygen_candidates, co2_candidates)
print(int(oxygen_candidates[0], 2) * int(co2_candidates[0], 2))