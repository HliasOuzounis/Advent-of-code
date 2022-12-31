def find_index(num_list, index):
    for new_i, (num, i) in enumerate(num_list):
        if i == index:
            return num, new_i  

def main():
    num_list = list(map(int, open("input.txt")))
    zero = num_list.index(0)
    key = 811589153
    num_list[:] = [(num * key, index) for index, num in enumerate(num_list)]
    list_len = len(num_list)
    for _i in range(10):
        for index in range(list_len):
            num, i = find_index(num_list, index)
            offset = abs(num) % (list_len - 1) * (1 if num > 0 else -1)
            new_index = offset + i

            if new_index >= list_len:
                new_index = new_index % list_len + 1
            if new_index == 0 and num < 0:
                new_index = list_len
            num_list.pop(i)
            num_list.insert(new_index, (num, index))

    zero = num_list.index((0, zero))
    print(sum(num_list[(zero + i * 1000) % list_len][0] for i in (1, 2, 3)))


if __name__ == "__main__":
    main()
