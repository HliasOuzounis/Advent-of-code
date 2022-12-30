from os import error


with open ("10/inputs.txt") as f:
    inp = f.readlines()

inp[:] = [line.strip("\n") for line in inp]

opening_chars = ["(", "[", "{", "<"]
closing_chars = [")", "]", "}", ">"]

errors = [3, 57, 1197, 25137]
error_sum = 0

for n, line in enumerate(inp):
    close = []
    for char in line:
        if char in opening_chars:
            close.append(closing_chars[opening_chars.index(char)])
        else:
            if char == close[-1]: 
                close.pop()
                continue
            else: 
                error_sum += errors[closing_chars.index(char)]
                break

print(error_sum)
