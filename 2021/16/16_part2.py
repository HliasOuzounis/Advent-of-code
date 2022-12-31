
with open ("16/inputs.txt") as f:
    inp = f.readline().strip("\n")

def pop_n_times(stack, n):
    val = ""
    for i in range(n):
        val += stack.pop()
    return val

def get_packet_values(stack):
    version = int(pop_n_times(stack, 3), 2)
    packet_id = pop_n_times(stack, 3)

    if packet_id == "100": 
        return get_literal_value(stack)
    else:
        sub_packets_values = []
        len_id = stack.pop()
        if len_id == '0':
            length = int(pop_n_times(stack, 15), 2)
            starting_stack_size = len(stack)
            while starting_stack_size - len(stack) < length:
                sub_packets_values.append(get_packet_values(stack))

        elif len_id == '1':
            nof_sub_packets = int(pop_n_times(stack, 11), 2)
            for i in range(nof_sub_packets):
                sub_packets_values.append(get_packet_values(stack))

        if packet_id == "000": return sum(sub_packets_values)
        if packet_id == "001": 
            prod = 1
            for val in sub_packets_values: prod *= val
            return prod
        if packet_id == "010": return min(sub_packets_values)
        if packet_id == "011": return max(sub_packets_values)
        if packet_id == "101": return sub_packets_values[0] > sub_packets_values[1]
        if packet_id == "110": return sub_packets_values[0] < sub_packets_values[1]
        if packet_id == "111": return sub_packets_values[0] == sub_packets_values[1]

def get_literal_value(stack):
    num = ""
    while stack.pop() == "1":
        num += pop_n_times(stack, 4)
    num += pop_n_times(stack, 4)
    return int(num, 2)

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

print(get_packet_values(binary_stack))