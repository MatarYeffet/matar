def Binary_representation_and_operations(num, bits=8):
    binary_num = bin(num)[2:].zfill(bits)
    print(f"Positive binary ({bits} bits): {binary_num}")
    binary_num_list = list(binary_num)
    for i in range(len(binary_num_list)):
        if binary_num_list[i] == '0':
            binary_num_list[i] = '1'
        else:
            binary_num_list[i] = '0'
    print(f"One's complement: {''.join(binary_num_list)}")
    carry = 1
    for i in range(len(binary_num_list) - 1, -1, -1):
        if binary_num_list[i] == '0' and carry == 1:
            binary_num_list[i] = '1'
            carry = 0
            break
        elif binary_num_list[i] == '1' and carry == 1:
            binary_num_list[i] = '0'
            carry = 1
        else:
            break
    negative_binary = ''.join(binary_num_list)
    print(f"Two's complement (negative): {negative_binary}")
    return negative_binary


Binary_representation_and_operations(1,bits=8)
