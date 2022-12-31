def main():
    num_list = list(map(lambda x: (int(x), True), open("input.txt")))
    list_len = len(num_list)
    index = 0
    while any(num[1] for num in num_list[::-1]):
        num, move = num_list.pop(index)
        if not move:
            num_list.insert(index, (num, False))
            index += 1
            continue

        offset = abs(num) % (list_len - 1) * (1 if num > 0 else -1)
        new_index = offset + index

        if new_index >= list_len: new_index = new_index % list_len + 1
        if new_index == 0 and num < 0: new_index = list_len
        num_list.insert(new_index, (num, False))
    
    print(num_list)
    zero = num_list.index((0, False))
    print(sum(num_list[(zero + i * 1000) % list_len][0] for i in (1, 2, 3)))
    

if __name__ == "__main__":
    main()