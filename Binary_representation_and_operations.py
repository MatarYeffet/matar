def Binary_representation_and_operations(num):
    g = 0
    binary_num = bin(num)[2:]
    for i in range(len(binary_num)):
        if binary_num[i] == 0:
            binary_num[i] = 1
        else:
            binary_num[i] = 0
    while binary_num[g] != binary_num[-1]:
        if binary_num[g] == 0:
            binary_num[g] = 1
            break
        else:
            binary_num[g] = 0
            g += 1
    print(binary_num)


Binary_representation_and_operations(10)
