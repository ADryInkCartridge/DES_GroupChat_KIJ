from Utils import *

left_rotations = [
    1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1
]

Compression_Table = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

Drop_Table = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]


def key_transformation(bin_key):
    
    bin_key = substitution(bin_key,Drop_Table)
    
    left_key, right_key = split_key(bin_key)
    
    compressed_key = [] 

    for i in range(16):

        left_key = left_shift(left_key, left_rotations[i])
        right_key = left_shift(right_key, left_rotations[i])
        key = left_key + right_key
        compressed_key.append(substitution(key, Compression_Table))

    return compressed_key

def left_shift(key,shift):
    return key[shift:] + key[:shift]

