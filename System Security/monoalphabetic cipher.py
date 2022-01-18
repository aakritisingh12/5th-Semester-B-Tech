Plain = "abcdefghijklmnopqrstuvwxyz"
Cipher = "DKVQFIBJWPESCXHTMYAUOLRGZN"
text = input("Enter your text: ")
ans = ""
for letter in text:
    if letter == " ":
        ans += letter
    elif letter.isupper():
        ans += Cipher[ord(letter)-65]
    else:
        ans += Cipher[ord(letter) - 97]

print("Converted text:", ans)
