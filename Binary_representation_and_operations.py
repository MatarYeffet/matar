def Binary_representation_and_operations(num):
    binary_num = bin(num)[2:]
    for i in range(len(binary_num)):
        if binary_num[i] == 0:
            binary_num[i] = 1
        else:
            binary_num[i] = 0
    str ""


Binary_representation_and_operations(10)
