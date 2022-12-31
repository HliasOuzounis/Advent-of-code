from functools import lru_cache
with open("input.txt") as f:
    inp = f.readlines()
inp[:] = [line.strip().split(" ") for line in inp]

def compute(z, digit, pos):
    command = inp[pos]
    if int(command[0]):
        if (z % 26) + int(command[1]) != digit:
            z += digit + int(command[2])
        else: z = z//26
    else:
        z *= 26
        z += digit + int(command[1])
    return z
    # return z * 26 + digit + int(command[1])

def find_mod(z, pos):
    command = inp[pos]
    d = z % 26 + int(command[1])
    return d if (d < 10 and d > 0) else None

digits = []

@lru_cache(maxsize = 1_000_000)
def find_max_num(z, pos):
    if pos == 14:
        if z == 0:
            return True
        else: return False
    if int(inp[pos][0]):
        digit = find_mod(z, pos)
        if digit:
            if find_max_num(z//26, pos + 1):
                digits.append(digit)
                return True
            else: return False
        else: return False
    else:
        for i in range(9, 0, -1):
            if find_max_num(compute(z, i, pos), pos + 1):
                digits.append(i)
                return True
        return False
        
find_max_num(0, 0)
digits.reverse()
for d in digits: print(d, end="")
