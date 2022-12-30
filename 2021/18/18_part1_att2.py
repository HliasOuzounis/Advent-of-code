with open ("18/inputs.txt") as f:
    inp = f.readlines()
inp[:] = [line.strip("\n") for line in inp]

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
                    fish_num.append([temp.copy(), nested_level])
                    temp = []
                    append_next = False
            nested_level += 1
        elif char == "]": 
            if append_next:
                if temp:
                    fish_num.append([temp.copy(), nested_level])
                    temp = []
                append_next = False
            nested_level -= 1
        elif char.isdigit(): temp.append(int(char))
        elif char == ",": append_next = True
        
    fish_nums_list.append(fish_num.copy())

def explode(num):
    for pos, (pair, depth) in enumerate(num):
        if depth > 4: 
            if len(pair) > 1:
                if pos > 0:
                    num[pos - 1][0][-1] += pair[0]
                if pos < len(num) - 1:
                    num[pos + 1][0][0] += pair[1]
                num[pos] = [[0], depth - 1]
                return True
    return False

def split(num):
    for pos, (pair, depth) in enumerate(num):
        for p, n in enumerate(pair):
            if n >= 10:
                half = n//2
                if len(pair) == 1:
                    num[pos] = [[half, n - half], depth + 1]
                else: 
                    num[pos][0].remove(n)
                    num.insert(pos + 1 * p, [[half, n - half], depth + 1])
                return True
    return False

def reduce_num(num):
    can_explode = True
    can_split = True
    while can_explode or can_split:
        can_explode = explode(num)
        if can_explode: 
            join_neighbours(num)
            continue
        can_split = split(num)
        join_neighbours(num)
    return num

def join_neighbours(num):
    for pos, (pair, depth) in enumerate(num):
        if len(pair) == 1:
            if pos < len(num) - 1:
                if len(num[pos+1][0]) == 1 and num[pos+1][1] == depth:
                    if pos == 0:
                        num[pos] = [pair + num[pos+1][0], depth]
                        del num[pos+1]
                    elif num[pos-1][1] != depth + 1:
                        num[pos] = [pair + num[pos+1][0], depth]
                        del num[pos+1]
            
def add_nums(nums_list):
    s = []
    for pos, num in enumerate(nums_list):
        s += num
        if pos > 0:
            for p in range(len(s)):
                s[p][1] += 1
            s = reduce_num(s)
    return(s)

def make_pairs(num):
    changed = False
    for pos, (pair, depth) in enumerate(num):
        if pos < len(num) - 1:
            if len(pair) == 2:
                if depth == num[pos+1][1] and len(num[pos+1][0]) == 2:
                    num[pos] = [[pair, num[pos+1][0]], depth - 1]
                    del num[pos+1]
                    changed = True
                elif depth == num[pos+1][1] - 1 and len(num[pos+1][0]) == 1:
                    num[pos] = [[pair, num[pos+1][0]], depth - 1]
                    del num[pos+1]
                    changed = True
            else:
                if depth == num[pos+1][1] - 1 and len(num[pos+1][0]) == 2:
                    num[pos] = [[pair, num[pos+1][0]], depth]
                    del num[pos+1]
                    changed = True
                elif depth == num[pos+1][1] and len(num[pos+1][0]) == 1:
                    num[pos] = [[pair, num[pos+1][0]], depth]
                    del num[pos+1]
                    changed = True
    if changed: return make_pairs(num)
    else: return num[0][0]


def find_magnitude(pair):
    if isinstance(pair, int):
        return int(pair)
    if len(pair) == 1: return int(pair[0])
    return 3 * find_magnitude(pair[0]) + 2 * find_magnitude(pair[1])

s = add_nums(fish_nums_list)
print(s)
pairs = make_pairs(s)
print(pairs)
magnitude = find_magnitude(pairs)
print(magnitude)
