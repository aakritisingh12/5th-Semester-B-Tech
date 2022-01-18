import numpy as np

a = input("Enter the text for encryption")
text = a
cols = 7
key = [4, 3, 1, 2, 5, 6, 7]

text = text.lower()
text = text.replace(" ", "")

pt_array = [char for char in text]
pt_array = np.array(pt_array)

sz_array = (int(len(pt_array) / cols))

for i in range(122 - sz_array + 1, 123):
    pt_array = np.append(pt_array, chr(i))

# Plaintext_array

pt_array = pt_array.reshape(4, 7)

ciphertext = []

for i in range(len(key)):
    col = key[i] - 1
    ciphertext = np.append(ciphertext, pt_array[:, col])

# Cypher_Text

cipherstring = ""
for element in ciphertext:
    cipherstring += element

print(cipherstring)
