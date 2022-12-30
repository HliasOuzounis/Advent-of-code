with open ("18/inputs.txt") as f:
    inp = f.readlines()
inp[:] = [line.strip("\n") for line in inp]

def explode(num):
    for pos, (pair, depth) in enumerate(num):
        if depth >= 4:
            if len(pair) > 1 and not 0 in pair:
                if pos > 0:
                    num[pos - 1][0][-1] += pair[0]
                if pos < len(num) - 1:
                    num[pos + 1][0][0] += pair[1]
                if pos > 0:
                    if len(num[pos - 1][0]) == 1 and num[pos - 1][1] == depth - 1:
                        num[pos - 1][0].append(0)
                        del num[pos]
                    else: num[pos] = [[0], depth - 1]
                elif pos < len(num) - 1:
                    if len(num[pos + 1][0]) == 1:
                        num[pos + 1][0].insert(0, 0)
                        del num[pos] 
                    else: num[pos] = [[0], depth - 1]
                exploded = True
                break
    else: exploded = False

    return num, exploded

def split_num(num):
    for pos, (pair, depth) in enumerate(num):
        for p, n in enumerate(pair):
            if n >= 10:
                half = n//2
                if len(pair) > 1:
                    num[pos][0].remove(n)
                    num.insert(pos + 1 * p, [[half, n - half], depth + 1])
                else:
                    num[pos] = [[half, n - half], depth + 1]
                return num, True
    return num, False

def reduce_fish_num(num, pos):
    can_explode = True
    can_split = True
    while can_explode or can_split:
        num, can_explode = explode(num)
        if can_explode: 
            if pos == 2: print(num)
            continue
        num, can_split = split_num(num)
        if pos == 2: print(num)
    return num

def magnitude(num):
    pass

def add_nums(nums_list):
    s = []
    for pos, num in enumerate(nums_list):
        s += num
        if pos > 0:
            for p in range(len(s)):
                s[p][1] += 1
        print(pos)
        s = reduce_fish_num(s, pos)
    return(s)

def print_fish_num(num):
    depth = 0
    for pair, d in num:
        while depth < d: 
            depth += 1
            print("[", end = "")
        while depth > d:
            depth -= 1
            print("],", end = "")
        print(pair, end = ",")
    while depth > 0:
        depth -= 1
        print("],", end = "")
    print("")


fish_nums_list = []
nested_level = 0
for line in inp:
    fish_num = []
    temp = []
    append_next = False
    for char in line:
        if char == "[": 
            if append_next:
                if temp:
                    fish_num.append([temp.copy(), nested_level - 1])
                    temp = []
                    append_next = False
            nested_level += 1
        elif char == "]": 
            if append_next:
                if temp:
                    if len(temp) == 1:
                        fish_num.append([temp.copy(), nested_level])
                        temp = []
                    else:
                        fish_num.append([temp.copy(), nested_level - 1])
                        temp = []
                append_next = False
            nested_level -= 1
        elif char.isdigit(): temp.append(int(char))
        elif char == ",": append_next = True
        

    fish_nums_list.append(fish_num.copy())

print(add_nums(fish_nums_list))