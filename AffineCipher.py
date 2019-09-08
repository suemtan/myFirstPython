#Coding_Assignment 1 (CS-265)
#Professor : Fabio Di Troia
#Su Tan
#February 15, 2019

from string import ascii_lowercase

from operator import itemgetter, attrgetter

#find greatest common divisor using recursive
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

lower = ascii_lowercase


def encrypt_affinecipher(plaintext, a, b):

    if gcd(a, 26) != 1:
        raise ValueError('a and 26 are not coprime. Please try again.')

    ciphertext = ''
    count = 1


    for char in plaintext:

        if char.isalpha():
            y = ((a * lower.index(char)) + b) % 26
            ciphertext += lower[y]

        else:
            ciphertext += char

    return ciphertext.strip()

def frequency_cipher(cipher):

    #for frequency count
    freq_string ={}

    for i in cipher:
        keys = freq_string.keys()
        if i in keys:
            freq_string[i] += 1
        else:
            freq_string[i] = 1

    return freq_string


# First string
print ("\nPlain text 1 : " + "helloworld")
print ("Ciphertext   : " + str(encrypt_affinecipher('helloworld', 3, 11)))

# letter frequency count
freq_str = {}
freq_str = encrypt_affinecipher('helloworld', 3, 11)

#print result frequency
print("Frequency Count :" + str(frequency_cipher(freq_str)))


# Second string
print ("\nPlain text 2 : " + "password answer is here")
print ("Ciphertext   : " + str((encrypt_affinecipher('password answer is here', 3, 11))))

# letter frequency count
freq_str2 = {}
freq_str2 = encrypt_affinecipher('password answer is here', 3, 11)

#print result frequency
print("Frequency Count :" + str(frequency_cipher(freq_str2)))


# Third string
print("\nPlain text 3 : " + "a an the a an the this that have has had a an the a an the this that have has had")
print("Ciphertext   : " + str(encrypt_affinecipher('a an the a an the this that have has had a an the a an the this that have has had',3, 11)))

# letter frequency count
freq_str3 = {}
freq_str3 = encrypt_affinecipher('a an the a an the this that have has had a an the a an the this that have has had', 3, 11)

#print result frequency
print("Frequency Count :" + str(frequency_cipher(freq_str3)))


# Fourth string
print ("\nPlain text 4 : " + "this message will transform into ciphertext and bring back to plaintext with key from receiver side")
print ("Ciphertext   : " + str((encrypt_affinecipher('this message will transform into ciphertext and bring back to plaintext with key from receiver side', 3, 11))))

# letter frequency count
freq_str4 = {}
freq_str4 = encrypt_affinecipher('this message will transform into ciphertext and bring back to plaintext with key from receiver side', 3, 11)

#print result frequency
print("Frequency Count :" + str(frequency_cipher(freq_str4)))


# Fifth string
print ("\nPlain text 5 : " + "bring the package that you need to deliver to the destination and give you more packages and information of next step")
print ("Ciphertext   : " + str((encrypt_affinecipher('bring the package that you need to deliver to the destination and give you more packages and of next step', 3, 11))))

# letter frequency count
freq_str5 = {}
freq_str5 = encrypt_affinecipher('bring the package that you need to deliver to the destination and give you more packages and next step', 3, 11)

#print result frequency
print("Frequency Count :" + str(frequency_cipher(freq_str5)))

# Sixth string
print ("\nPlain text 6 : " + "meet me at warmspring bart station on february twenty at seven thirty in the morning and wear the blue color blouse and kaki pant")
print ("Ciphertext   : " + str((encrypt_affinecipher('meet me at warmspring bart station on february twenty at seven thirty in the morning and wear the blue color blouse and kaki pant', 3, 11))))

# letter frequency count
freq_str6 = {}
freq_str6 = encrypt_affinecipher('meet me at warmspring bart station on february twenty at seven thirty in the morning and wear the blue color blouse and kaki pant', 3, 11)

#print result frequency
print("Frequency Count :" + str(frequency_cipher(freq_str6)))

# ciphertext encryption for (string, a, b)

