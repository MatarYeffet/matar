def Binary_representation_and_operations(num):
    g = 0
    binary_num = bin(num)[2:]
    binary_num_list = list(binary_num)
    for i in range(len(binary_num_list)):
        if binary_num_list[i] == 0:
            binary_num_list[i] = 1
        else:
            binary_num_list[i] = 0
    while binary_num_list[g] != binary_num_list[-1]:
        if binary_num_list[g] == 0:
            binary_num_list[g] = 1
            break
        else:
            binary_num_list[g] = 0
            g += 1
    binary_representation_of_a_negative_number = ''.join(str(bit) for bit in binary_num_list)
    print(binary_representation_of_a_negative_number)


Binary_representation_and_operations(10)
