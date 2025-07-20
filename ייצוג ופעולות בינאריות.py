def decimal_to_twos_complement(num, bits):
    if num >= 2**(bits - 1):
        raise ValueError("המספר גדול מדי לגודל הזיכרון שנבחר")
    twos_complement = (1 << bits) - num
    return format(twos_complement, f'0{bits}b')


#decimal_to_twos_complement(10,2)