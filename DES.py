from Utils import *
import Keys
import Feistel

def DES_Encrypt(plaintext, key):
    # pad plaintext
    plaintext = pad_plaintext(plaintext)

    # Convert plaintext and key to binary
    bin_plaintext = str_to_bin(plaintext)
    bin_key = hex_to_bin(key)

    # Split key into two halves
    # print('Padded_plaintext: ', plaintext)
    # print('Key_Bin: ', bin_key)
    # print('Plaintext_Bin: ', bin_plaintext)
    # print('Bin length: ', len(bin_plaintext))

    # Key Transformation
    transformed_key = Keys.key_transformation(bin_key)
    cipher = Feistel.encrypt(bin_plaintext, transformed_key)
    return cipher

def DES_Decrypt(ciphertext, key):
    
    bin_cipher = str_to_bin(ciphertext)
    bin_key = hex_to_bin(key)

    # print('Key_Bin: ', bin_key)
    # print('Cipher_bin: ', bin_cipher)
    # print('Bin length: ', len(bin_cipher))
    transformed_key = Keys.key_transformation(bin_key)
    reversed_key = transformed_key[::-1]

    decrypted = Feistel.encrypt(bin_cipher, reversed_key)
    return decrypted
    
