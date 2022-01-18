P10_table = (3, 5, 2, 7, 4, 10, 1, 9, 8, 6)
P8_table = (6, 3, 7, 4, 8, 5, 10, 9)
EP_table = (4, 1, 2, 3, 2, 3, 4, 1)
P4_table = (2, 4, 3, 1)
FIXED_IP = (2, 6, 3, 1, 4, 8, 5, 7)
FIXED_IP_INVERSE = (4, 1, 3, 5, 7, 2, 8, 6)


sbox_1 = [[1, 0, 3, 2],
          [3, 2, 1, 0],
          [0, 2, 1, 3],
          [3, 1, 3, 2]]

sbox_2 = [[0, 1, 2, 3],
          [2, 0, 1, 3],
          [3, 0, 1, 0],
          [2, 1, 0, 3]]

KEY = '0001101101'


def permutate(original, fixed_key):
    return ''.join(original[i - 1] for i in fixed_key)


def left_half(bits):
    return bits[:len(bits)//2]


def right_half(bits):
    return bits[len(bits)//2:]


def shift(bits):
    rotated_left_half = left_half(bits)[1:] + left_half(bits)[0]
    rotated_right_half = right_half(bits)[1:] + right_half(bits)[0]
    return rotated_left_half + rotated_right_half


def key1():
    return permutate(shift(permutate(KEY, P10_table)), P8_table)


def key2():
    return permutate(shift(shift(shift(permutate(KEY, P10_table)))), P8_table)


def xor(bits, key):
    return ''.join(str(((bit + key_bit) % 2)) for bit, key_bit in
                   zip(map(int, bits), map(int, key)))


def lookup_in_sbox(bits, sbox):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)
    return '{0:02b}'.format(sbox[row][col])


def f_k(bits, key):
    l = left_half(bits)
    r = right_half(bits)
    bits = permutate(r, EP_table)
    bits = xor(bits, key)
    bits = lookup_in_sbox(left_half(bits), sbox_1) + lookup_in_sbox(right_half(bits), sbox_2)
    bits = permutate(bits, P4_table)
    return xor(bits, l)


def encrypt(plain_text):
    bits = permutate(plain_text, FIXED_IP)
    temp = f_k(bits, key1())
    bits = right_half(bits) + temp
    bits = f_k(bits, key2())
    print("Encrypted text: ", permutate(bits + temp, FIXED_IP_INVERSE))


def decrypt(cipher_text):
    bits = permutate(cipher_text, FIXED_IP)
    temp = f_k(bits, key2())
    bits = right_half(bits) + temp
    bits = f_k(bits, key1())
    print("Decrypted Text: ", permutate(bits + temp, FIXED_IP_INVERSE))


print("Plain text: 10100001")
encrypt('01000010')
decrypt('00101011')
