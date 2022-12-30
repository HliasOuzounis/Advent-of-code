with open("3\inputs.txt") as f:
    report = f.readlines()

# report[:] = [bits.split() for bits in report]
bit_len = len(str(report[0])) - 2
bit_sums = [0] * bit_len
for bits in report:
    for pos, bit in enumerate(str(bits)[:-2]):
        bit_sums[pos] += int(bit)

gamma = "".join(str(round(sum / len(report))) for sum in bit_sums)
epsilon = "".join(str(1 - round(sum / len(report))) for sum in bit_sums)

print(epsilon, gamma)
print(int(int(gamma, 2)) * int(int(epsilon, 2)))
