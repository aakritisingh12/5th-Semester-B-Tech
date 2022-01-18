def encryptRailFence(text, key):

    rail = [['\n' for i in range(len(text))]
            for j in range(key)]

    direction = False
    row, col = 0, 0

    for i in range(len(text)):

        if (row == 0) or (row == key - 1):
            direction = not direction

        rail[row][col] = text[i]
        col += 1

        if direction:
            row += 1
        else:
            row -= 1

    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return "".join(result)


# This function receives cipher-text and key and returns the original text after decryption
def decryptRailFence(cipher, key):

    rail = [['\n' for i in range(len(cipher))]
            for j in range(key)]

    direction = None
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            direction = True
        if row == key - 1:
            direction = False

        rail[row][col] = '*'
        col += 1

        if direction:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
                    (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(cipher)):

        if row == 0:
            direction = True
        if row == key - 1:
            direction = False

        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1

        if direction:
            row += 1
        else:
            row -= 1
    return "".join(result)


print("*************Encryption*************")
print("Plaintext: I love my country\nRows: 3")
print("Output: ", encryptRailFence("ILOVEMYCOUNTRY", 3))

# Now decryption of the same cipher-text
print("\n\n*************Decryption*************")
print("Ciphertext: IEORLVMCUTYOYN\nRows: 3")
print("Output: ", decryptRailFence("IEORLVMCUTYOYN", 3))
