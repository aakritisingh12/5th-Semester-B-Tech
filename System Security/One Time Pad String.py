letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
text = input('Enter Plain Text: ')
key = input("Enter key: ")
cipher = ""
for i in range(len(text)):
    sm = letters.index(text[i]) + letters.index(key[i])
    if sm > 25:
        sm -= 26
    cipher += letters[sm]

print("Encrypted Text = ", cipher)

decrypt = ""
for i in range(len(cipher)):
    sb = letters.index(cipher[i]) - letters.index(key[i])
    if sb < 0:
        sb += 26
    decrypt += letters[sb]

print("Decrypted Text = ", decrypt)
