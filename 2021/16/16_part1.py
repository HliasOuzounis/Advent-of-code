
with open ("16/inputs.txt") as f:
    inp = f.readline().strip("\n")

def pop_n_times(stack, n):
    val = ""
    for i in range(n):
        val += stack.pop()
    return val

def get_packet_versions(stack):
    version = int(pop_n_times(stack, 3), 2)
    packet_id = pop_n_times(stack, 3)

    if packet_id == "100": 
        get_literal_value(stack)
        return version
    else:
        sub_packets_version_sum = 0
        len_id = stack.pop()
        if len_id == '0':
            length = int(pop_n_times(stack, 15), 2)
            starting_stack_size = len(stack)
            while starting_stack_size - len(stack) < length:
                sub_packets_version_sum += get_packet_versions(stack)

        elif len_id == '1':
            nof_sub_packets = int(pop_n_times(stack, 11), 2)
            for i in range(nof_sub_packets):
                sub_packets_version_sum += get_packet_versions(stack)

        return sub_packets_version_sum + version

def get_literal_value(stack):
    num = ""
    while stack.pop() == "1":
        num += str(int(pop_n_times(stack, 4), 2))
    num += str(int(pop_n_times(stack, 4), 2))
    return num

binary0 = []
for ch in inp:
    binary0.append(bin(int(ch, 16))[2:])

binary = []
for b in binary0:
    if len(b) < 4:
        b = b.zfill(4)
    for i in b:
        binary.append(i)

binary_stack = binary[::-1]

print(get_packet_versions(binary_stack))

            

