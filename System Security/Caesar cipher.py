def encrypt(text, shift):
    ans = ""
    for letter in text:
        if letter == " ":
            ans += letter
        elif letter.isupper():
            ans += chr((ord(letter) + shift - 65) % 26 + 65)
        else:
            ans += chr((ord(letter) + shift - 97) % 26 + 97)
    return ans


plain_text = input("Enter your text: ")
key = int(input("Enter shift: "))
print("Cipher Text: " + encrypt(plain_text, key))
