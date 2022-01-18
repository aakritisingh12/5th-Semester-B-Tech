# DES Encryption and decryption algorithm implementation
# Completed: Encrypted for the first time

# Plaintext replacement
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]
IP_1 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

# Plaintext expansion permutation
E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

# Plaintext permutation function
P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

# Key replacement option 1
PC_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

# Key replacement option 1
PC_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]

# S box
S = [
    # S1
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

    # S2
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

    # S3
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

    # S4
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

    # S5
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

    # S6
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

    # S7
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

    # S8
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]],
]

# Key shift times
LeftRotate = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


# 1. Clear text processing
# Read the plaintext into the program and turn it into a binary string
# Enter the plaintext and get the binary bits of the plaintext stored in the list
def inputText(filename):
    with open(filename, 'r')as f:
        text = f.read()
    text = text.split('\n')
    text = [eval(x) for x in text]
    text = ['{:08b}'.format(x) for x in text]
    # for x in text:
    #     print(x)
    text = ''.join(text)
    # print(text)
    return text


# Perform IP permutation on the plaintext and divide it into two left and right substrings
# IP replacement of plaintext
# i position corresponds to the array index i-1
def IP_Transposition(plaintext):
    LR = []
    for i in IP:
        LR.append(int(plaintext[i - 1]))
    L = LR[:32]
    R = LR[32:]
    return L, R


# Inverse permutation
def IP_reverseTransp(LR):
    tmp = []
    for i in IP_1:
        tmp.append(LR[i - 1])
    return tmp


# Enter key
def inputKey(s):
    with open(s, 'r')as f:
        key = f.read()
    key = key.split('\n')
    key = [eval(x) for x in key]
    key = ['{:08b}'.format(x) for x in key]
    key = "".join(key)
    return key


# Handling of keys
# Read the key into the program and store it in the form of a binary string
# Perform PC-1 permutation on the key and divide it into two substrings
# Key replacement
def Key_Transposition(key):
    CD = []
    for i in PC_1:
        CD.append(int(key[i - 1]))
    C = CD[:28]
    D = CD[28:]
    return C, D


# Key rotation left
def Key_LeftRotate(key, n):
    new_key = key[n:]
    for i in range(0, n):
        new_key.append(key[i])
    return new_key


# It is necessary to perform permutation compression on the key before generating the key required for the iteration
# Key compression
def Key_Compress(C, D):
    key = C + D
    new_key = []
    for i in PC_2:
        new_key.append(key[i - 1])
    return new_key


# Generate ciphertext from list
def generateHex(LR):
    result = []
    for i in range(0, 8):
        result.append(
            LR[8 * i] * 128 + LR[8 * i + 1] * 64 + LR[8 * i + 2] * 32 + LR[8 * i + 3] * 16 + LR[8 * i + 4] * 8 + LR[
                8 * i + 5] * 4 + LR[8 * i + 6] * 2 + LR[8 * i + 7])
    result = [hex(x) for x in result]
    return result


# In each round of transformation, the entire process can be expressed by the following formula: L_i = R_{i-1}

# R_i = L_{i-1}\i F(R_{i-1},K_i)

# The round key K_i is 48 bits long and R is 32 bits long. First, the $R$ replacement is expanded to 48 bits.
# These 48 bits are XORed with K_i, and the result obtained is used as a substitute function to generate a 32-bit Output.
# The 32-bit output is XORed with L_{i-1} after being replaced by P to get a new R_i

# The replacement function is composed of 8 S boxes, each S box has 6 bits of input and 4 bits of output. For each S box,
# the first and last digits of the input form a 2-digit binary number, which is used to select one of the four-row
# replacement values of the S box, and the middle 4 digits are used to select the 16-column A certain column.

# Expansion of plain text R to 48 bits
def R_expand(R):
    new_R = []
    for i in E:
        new_R.append(R[i - 1])
    return new_R


# XOR the elements of two lists
def xor(input1, input2):
    xor_result = []
    for i in range(0, len(input1)):
        xor_result.append(int(input1[i]) ^ int(input2[i]))
    return xor_result


# Replace the result of XOR with S-box
def S_Substitution(xor_result):
    s_result = []
    for i in range(0, 8):
        tmp = xor_result[i * 6:i * 6 + 5]
        row = tmp[0] * 2 + tmp[-1]
        col = tmp[1] * 8 + tmp[2] * 4 + tmp[3] * 2 + tmp[4]
        s_result.append('{:04b}'.format(S[i][row][col]))
    s_result = ''.join(s_result)
    return s_result


# F function
def F(R, K):
    new_R = R_expand(R)
    R_Kxor = xor(new_R, K)
    s_result = S_Substitution(R_Kxor)
    p_result = P_Transposition(s_result)
    return p_result


# Perform P permutation on the result of S-box substitution
def P_Transposition(s_result):
    p_result = []
    for i in P:
        p_result.append(int(s_result[i - 1]))
    return p_result


# Write ciphertext to file
def writeFile(filename, Cipher):
    f = open(filename, 'w+')
    for i in range(len(Cipher) - 1):
        f.write(Cipher[i] + '\n')
    f.write(Cipher[-1])


# Generate the sub-keys required for each iteration of DES for direct use in encryption and decryption
# Generate Kset,
def generateKset(key):
    key = inputKey(key)
    C, D = Key_Transposition(key)
    K = []
    for i in LeftRotate:
        C = Key_LeftRotate(C, i)
        C = Key_LeftRotate(D, i)
        K.append(Key_Compress(C, D))
    return K


# Encryption process

# DES encryption needs to go through 16 iterations, the first 15 iterations need to exchange L_i and R_i at the
# end of each iteration, and no exchange at the 16th time
# The first round of encryption
def DES_encrypt(filename, key, outputFile):
    # Read plaintext from file
    plaintext = inputText(filename)
    # Permutation and separation of plaintext
    L, R = IP_Transposition(plaintext)
    # Generate Kset
    K = generateKset(key)
    for i in range(0, 15):
        oldR = R
        # F function
        p_result = F(R, K[i])
        R = xor(L, p_result)
        L = oldR
    p_result = F(R, K[15])
    L = xor(L, p_result)
    # IPReverse Permutation
    reversedP = IP_reverseTransp(L + R)
    # Generate ciphertext in hexadecimal representation
    Cipher = generateHex(reversedP)
    # Write the ciphertext to the outputFile file
    writeFile(outputFile, Cipher)
    return Cipher


# The second round of decryption
def DES_decrypt(filename, key, outputFile):
    # Read ciphertext from file
    Ciphertext = inputText(filename)
    # Permutation and separation of ciphertext
    L, R = IP_Transposition(Ciphertext)
    # generate Kset
    K = generateKset(key)
    for i in range(15, 0, -1):
        oldR = R
        # F function
        p_result = F(R, K[i])
        R = xor(L, p_result)
        L = oldR

    p_result = F(R, K[0])
    L = xor(L, p_result)
    reversedP = IP_reverseTransp(L + R)
    plaintext = generateHex(reversedP)
    writeFile(outputFile, plaintext)
    return plaintext


if __name__ == "__main__":
    # 3DES encryption
    with open('plaintext.txt', 'r')as f:
        text = f.read()
    text = text.split('\n')
    text = [eval(x) for x in text]
    print('Plaintext: ', [hex(x) for x in text])
    Cipher = DES_encrypt('plaintext.txt', 'key1.txt', 'cipher1.txt')
    plaintext = DES_decrypt('cipher1.txt', 'key2.txt', 'plaintext1.txt')
    Cipher = DES_encrypt('plaintext1.txt', 'key1.txt', 'Cipher.txt')
    print('Ciphertext: ', Cipher)

    # 3DES Decrypt
    Plaintext = DES_decrypt('Cipher.txt', 'key1.txt', 'plaintext2.txt')
    Cipher1 = DES_encrypt('plaintext2.txt', 'key2.txt', 'cipher2.txt')
    Plaintext = DES_decrypt('cipher2.txt', 'key1.txt', 'Plaintext.txt')
    print('Decrypted plaintext: ', Plaintext)

# Cipher = DES_encrypt('plaintext.txt','key1.txt')
# print('密文: ',Cipher)
# plaintext = DES_decrypt('Cipher1.txt','key2.txt')
# print('解密后的明文: ',plaintext)
# Cipher = DES_encrypt('plaintext1.txt','key1.txt')
# print('密文: ',Cipher)
