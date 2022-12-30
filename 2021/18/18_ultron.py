import math

inp = """..."""

def eval_lst(lst):
    if isinstance(lst, int):
        return lst
    return 3 * eval_lst(lst[0]) + 2 * eval_lst(lst[1])

def parse(res):
    # print(res)
    while 1:
        changes = 0
        opens = 0
        i = 0
        # print("restarted")
        while i < len(res):
            if res[i] == "[":
                opens += 1
                # print(opens)
            if res[i] == "]":
                opens -= 1
            if opens == 4:
                for j in range(i + 1, len(res)):
                    if res[j] == "]":
                        break
                    if res[j] == "[":
                        try:
                            a = res[j + 1:j + res[j:].index(",")].isdigit()
                            a = res[j + 1:res[j:].index(",")]
                        except:
                            continue

                        if res[j + 1:j + res[j:].index(",")].isdigit() and "[" not in res[j + 1:res[j:].index(",")]:
                            if not res[j + 1 + res[j:].index(",")].isdigit():
                                continue
                            # explode
                            left_number = -1
                            left_number_pos = []
                            right_number = -1
                            right_number_pos = []
                            end_limit = -1
                            for k in range(j, 0, -1):
                                # if res[k] == "]":
                                #     break
                                temp = k
                                if res[k].isdigit():
                                    while res[temp].isdigit():
                                        temp -= 1
                                    left_number = int(res[temp + 1:k + 1])
                                    left_number_pos = [temp + 1, k + 1]
                                    break
                            for k in range(j + 1 + res[j:].index("]"), len(res)):
                                # if res[k] == "[":
                                #     break
                                temp = k
                                if res[k].isdigit():
                                    while res[temp].isdigit():
                                        temp += 1
                                    right_number = int(res[k:temp])
                                    right_number_pos = [k, temp]
                                    end_limit = temp + 1
                                    break
                            # print(left_number, right_number)
                            first_number = int(res[j + 1:j + res[j:].index(",")])
                            second_number = int(res[j + 1 + res[j:].index(","): j + res[j:].index("]")])

                            # print("resa:", res)
                            if right_number >= 0:
                                new_number = second_number + right_number
                                res = res[:right_number_pos[0]] + str(new_number) + res[right_number_pos[1]:]
                                # res[right_number_pos[0] +res[right_number_pos[0]:].index(
                                #                                                       "]"):]
                            else:
                                res = res[:j + res[j:].index("]") + 1] + "0" + res[j + res[j:].index("]") + 1:]

                            res = res[:j] + res[j + res[j:].index("]") + 1:]
                            if res[j - 1] == "[" and res[j] == ",":
                                res = res[:j] + "0" + res[j:]
                            # print("resjjjjj:", res[j-1], res[j])
                            if res[j - 1] == "," and res[j] == "]":
                                res = res[:j] + "0" + res[j:]

                            if left_number >= 0:
                                new_number = first_number + left_number
                                # print(new_number)
                                res = res[:left_number_pos[0]] + str(new_number) + res[left_number_pos[1]:]
                            else:
                                # print("resj:", res[j])
                                pass

                            # print("after explode:", res)
                            changes = 1
                            break

            i += 1
            if changes:
                break
        index = 0
        while index in range(len(res)) and changes == 0:
            if res[index].isdigit():
                k = 0
                while index + k < len(res) and res[index + k].isdigit():
                    k += 1
                # print(k)
                if k > 1:
                    changes = 1
                    number = int(res[index:index + k])
                    res = res[:index] + "[{},{}]".format(math.floor(number / 2), math.ceil(number / 2)) + res[
                                                                                                          index + k:]
                    # print("after split:", res)
                    break
            index += 1
        # print("new_loop")
        if changes == 0:  # 0
            break
    return res


# Part1:

result = inp.split("\n")[0]

for line in inp.split("\n")[1:]:
    new_result = "[{},{}]".format(result, line).replace(" ", "")
    new_result = parse(new_result)

    result = new_result[:]
    # print("\n\n\nNew cycle:", result)

result = """print("Part 1:",eval_lst({}))""".format(result)
eval(result)

# Part2:

list_of_operands = inp.split("\n")
max_sum = 0
results = []
for op1 in list_of_operands:
    for op2 in list_of_operands:
        if op1 != op2:
            result = parse("[{},{}]".format(op1, op2).replace(" ", ""))
            result = "results.append(eval_lst({}))".format(result)
            eval(result)
print("Part 2:", max(results))
