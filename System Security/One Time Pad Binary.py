# Function to find the XOR of the two Binary Strings
def xor(a, b, n):
    ans = ""
    # Loop to iterate over the Binary Strings
    for i in range(n):
        # If the Character matches
        if a[i] == b[i]:
            ans += "0"
        else:
            ans += "1"
    return ans


# Driver Code
if __name__ == "__main__":
    plaintext = input("Enter Plain Text: ")
    key = input("Enter key: ")
    n = len(plaintext)
    cipher = xor(plaintext, key, n)
    print("Encrypted Text = ", cipher)
    decrypt = xor(cipher, key, n)
    print("Decrypted Text = ", decrypt)
