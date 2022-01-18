print("RSA ENCRYPTOR/DECRYPTOR")
print("*****************************************************")

# Input Prime Number
# print("PLEASE ENTER THE 'p' AND 'q' VALUES BELOW:")
p = int(input("Enter a prime number for p: "))
q = int(input("Enter a prime number for q: "))
# print("*****************************************************")


# Check if Input's are Prime
'''THIS FUNCTION AND THE CODE IMMEDIATELY BELOW THE FUNCTION CHECKS WHETHER THE INPUTS ARE PRIME OR NOT'''
def prime_check(a):
    if a == 2:
        return True
    elif (a < 2) or (a % 2 == 0):
        return False
    elif a > 2:
        for i in range(2, a):
            if not (a % i):
                return False
    return True


check_p = prime_check(p)
check_q = prime_check(q)
while check_p is False or check_q is False:
    p = int(input("Enter a prime number for p: "))
    q = int(input("Enter a prime number for q: "))
    check_p = prime_check(p)
    check_q = prime_check(q)

# RSA Modulus
'''CALCULATION OF RSA MODULUS 'n'.'''
n = p * q
print("RSA Modulus(n) is:", n)

# Euler's Toitent
'''CALCULATION OF EULER'S TOITENT 'r'.'''
r = (p - 1) * (q - 1)
print("Euler's Toitent(r) is:", r)
# print("*****************************************************")


# GCD
'''CALCULATION OF GCD FOR 'e' CALCULATION.'''
def GCD(e, r):
    while r != 0:
        e, r = r, e % r
    return e


# Euclid's Algorithm
def eugcd(e, r):
    for i in range(1, r):
        while e != 0:
            a, b = r // e, r % e
            # if b != 0:
            #     print(r, "=", a, "*(", e, ") +", b)
            r = e
            e = b


# Extended Euclidean Algorithm
def ExtendedEuclideanAlgorithm(a, b):
    if a % b == 0:
        return b, 0, 1
    else:
        gcd, s, t = ExtendedEuclideanAlgorithm(b, a % b)
        s = s - ((a // b) * t)
        # print(gcd, "=", a, "*(", t, ") + (", s, ")*(", b, ")")
        return gcd, t, s


# Multiplicative Inverse
def MultiplicativeInverse(e, r):
    gcd, s, _ = ExtendedEuclideanAlgorithm(e, r)
    if gcd != 1:
        return None
    else:
        if s < 0:
            print("s =", s, ". Since", s, "is less than 0, s = (modr), i.e., s =", s % r)
        elif s > 0:
            print("s =", s,)
        return s % r


# Value Calculation
'''FINDS THE HIGHEST POSSIBLE VALUE O3F 'e' BETWEEN 1 and 1000 THAT MAKES (e,r) COPRIME.'''
for i in range(1, 1000):
    if GCD(i, r) == 1:
        e = i
print("The value of e is: ", e)
# print("*****************************************************")

'''CALCULATION OF 'd', PRIVATE KEY, AND PUBLIC KEY.'''
# print("EUCLID'S ALGORITHM:")
eugcd(e, r)
# print("END OF THE STEPS USED TO ACHIEVE EUCLID'S ALGORITHM.")
# print("*****************************************************")
# print("EUCLID'S EXTENDED ALGORITHM:")
d = MultiplicativeInverse(e, r)
# print("END OF THE STEPS USED TO ACHIEVE THE VALUE OF 'd'.")
print("The value of d is:", d)
# print("*****************************************************")
public = (e, n)
private = (d, n)
print("Private Key is:", private)
print("Public Key is:", public)
# print("*****************************************************")


# Encryption
'''ENCRYPTION ALGORITHM'''
def encrypt(pub_key, encmsg):
    e, n = pub_key
    x = []
    m = 0
    for letter in encmsg:
        m = ord(letter)
        c = (m ** e) % n
        x.append(c)
        if letter.isupper():
            m = ord(letter) - 65
            c = (m**e) % n
            x.append(c)
        elif letter.islower():
            m = ord(letter) - 97
            c = (m**e) % n
            x.append(c)
        elif letter.isspace():
            c = 400
            x.append(400)
    return x


# Decryption
'''DECRYPTION ALGORITHM'''
def decrypt(priv_key, msg):
    d, n = priv_key
    txt = msg.split(',')
    x = ''
    m = 0
    for number in txt:
        if number == '400':
            x += ' '
        else:
            m = (int(number)**d) % n
            m += 65
            c = chr(m)
            # c = str(m)
            x += c
    return x


# Message
# message = input("What would you like encrypted or decrypted?(Separate numbers with ',' for decryption):")
message = input("Enter your message for Encryption or decryption: ")
# print("Your message is:", message)

# Choose Encrypt or Decrypt and Print
# choose = int(input("Type '1' for encryption and '2' for decryption."))
# if choose == 1:
#     enc_msg = encrypt(public, message)
#     print("Your encrypted message is :", enc_msg)
#     print("Thank you for using the RSA Encryptor.")# Goodbye!")
# elif choose == 2:
#     print("Your decrypted message is :", decrypt(private, message))
#     print("Thank you for using the RSA Encryptor.")# Goodbye!")
# else:
#     print("You entered the wrong option.")
#     print("Thank you for using the RSA Encryptor.")# Goodbye!")


enc_msg = encrypt(public, message)
print("Your encrypted message is :", enc_msg)
dec_msg = str(enc_msg)[1:len(str(enc_msg))-1]
print("Your decrypted message is :", decrypt(private, dec_msg))
