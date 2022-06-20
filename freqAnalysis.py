import numpy as np
import string


"""
We perform frquency attacks on
the shift and multiplicative cipher
as well as implement the Hill cipher.

@author: Rashad Salim Al-Harthy
"""



alpha = list(string.ascii_uppercase)

Z26 = [i for i in range(26)]

alpha_decode = dict(zip(Z26, alpha))

alpha_encode = dict(zip(alpha, Z26))


# this is Z26ˆ*\{1} both k and k' are in Z26ˆ*\{1}
key_space = [3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]


# returns the inverse of the encoded letter n
# i.e x st x*n(mod26) = 1
def getMultInverse(n):

    for i in range(len(key_space)):
        if (n*key_space[i])%26 == 1:
            return key_space[i]
            break
    return -1

def getMaxFreq(x):

    frequency_list = []

    for i in range(26):

        frequency_list.append(x.count(alpha_decode[i]))


    print(f'frequency list: \n {frequency_list}')

    return alpha_decode[np.argmax(frequency_list)]




"""
Function for decrypting the shift Cipher
using frequency analysis

Given that plaintext is in English:

Most frequent letters in order:

1. E
2. T
3. A


"""
def decrypt_shift(cipher_text):

    print(f'cipher text = {cipher_text}')


    freq_letter = getMaxFreq(cipher_text)

    # now freq_letter ===> 'E' or 'T' or 'A', y = P and x = E, hence key = (y-x)mod26

    key1 = (alpha_encode[freq_letter]-alpha_encode['E'])%26
    key2 = (alpha_encode[freq_letter]-alpha_encode['T'])%26
    key3 = (alpha_encode[freq_letter]-alpha_encode['A'])%26

    print(f'possible keys are : [{key1, key2, key3}]')

    plaintext1 = ''
    plaintext2 = ''
    plaintext3 = ''

    # now we transform the cipher text

    for i in range(0, len(cipher_text)):

        plain_letter1 = alpha_decode[(alpha_encode[cipher_text[i]] - key1)%26]
        plain_letter2 = alpha_decode[(alpha_encode[cipher_text[i]] - key2)%26]
        plain_letter3 = alpha_decode[(alpha_encode[cipher_text[i]] - key3)%26]

        plaintext1 += plain_letter1
        plaintext2 += plain_letter2
        plaintext3 += plain_letter3

    print(f'plaintext for key1: {plaintext1}')
    print(f'plaintext for key2: {plaintext2}')
    print(f'plaintext for key3: {plaintext3}')


def decrypt_multiplicative(cipher_text):


    most_freq_letter = 'P'

    # now freq_letter ===> x = 'T' or 'N' or 'R'
    # hence key = (y*inv(x))mod26

    keys = []
    list = [19, 13, 17]

    for item in list:

        key = (alpha_encode[most_freq_letter]*getMultInverse(item))%26

        invk = getMultInverse(key)

        if (invk != -1) & (key != 1) & (key != 0):
            keys.append(key)



    print(f'possible keys k are : {keys}')

    plaintext = ''

    # now we transform the cipher text back

    for i in range(len(keys)):

        for j in range(0, len(cipher_text)):

            plain_letter = alpha_decode[(alpha_encode[cipher_text[j]]*
            getMultInverse(keys[i])
            )%26]

            plaintext += plain_letter

        print(f'plaintext for key {i}: {plaintext}')

        plaintext = ''




def encode_matrix(A):

        A_encoded = np.zeros(A.shape, dtype=int)

        for i in range(len(A)):
            for j in range(len(A[i])):
                A_encoded[i,j] = alpha_encode[A[i,j]]

        return A_encoded

def decode_matrix(A):

        A_decoded = np.zeros(A.shape, dtype=int)

        for i in range(len(A)):
            for j in range(len(A[i])):
                A_decoded[i,j] = alpha_decode[A[i,j]]

        return A_decoded

def encode_vector(v):

    v_encoded = np.zeros(v.shape, dtype=int)

    for i in range(len(v)):
        v_encoded[i] = alpha_encode[v[i]]

    return v_encoded

def decode_vector(v):

    v_decoded = np.zeros(v.shape, dtype=object)

    for i in range(len(v)):
        v_decoded[i] = alpha_decode[v[i]]

    return v_decoded




def Hill_encrypt(plaintext):


    # this is the key

    K = np.array([['T', 'B', 'E'], ['C', 'H', 'E'], ['B', 'D', 'B']])

    K = encode_matrix(K)


    v = encode_vector(plaintext)

    cipher_text = np.dot(v, K)%26


    print(f'Cipher text is: {decode_vector(cipher_text)}')
