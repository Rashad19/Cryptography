"""
We Perform an Index of Coincidence test on the
Vigenere Cipher, this code is mainly to calulate the
Index of Coincidence for different key lengths


CommandLine arguments (inorder): crypto_text file, 5 key lengths to test.

Total CLAs = 6

@author: Rashad

"""


import string
import sys

# this creates a list of all the english
# letter alphabets in lowercase

alpha = list(string.ascii_lowercase)


# returns the sequences of letters encrypted by the same key
# this is crucial since I.C is calculated on them.
def getSequence(text, keylength):

    sequences = []


    for i in range(keylength):

        sequence = ''

        d = 0

        for j in range(len(text)):

            if i + d > len(text) - 1:
                break

            sequence += text[i+d]

            d += keylength

        sequences.append(sequence)

    return sequences



"""
This Calculates the Index of Coincidence
of a given crypto-text y
"""

def getCindex(y):

    freqs_sum = 0.

    for i in range(len(alpha)):

        freqs_sum += (y.count(alpha[i]))*(y.count(alpha[i])-1.)

    IC = ((1.)/(len(y)*(len(y)-1.)))*(freqs_sum)

    return IC

def main(args):

    d = []

    d.append(args[2])
    d.append(args[3])
    d.append(args[4])
    d.append(args[5])
    d.append(args[6])



    with open(args[1], 'r') as file:
        crypto_text = file.read().replace('\n','')

    print('Program to Calculate Index of Coincidence of Cryptotext y (IC(y))\n')
    print(f'Index of Coincidence for text in {args[1]} = {getCindex(crypto_text)}')
    print('performing Index of Coincidence test to find possible key length....\n')

    seq1 = getSequence(crypto_text,1)

    seq2 = getSequence(crypto_text,2)

    seq3 = getSequence(crypto_text,3)

    seq4 = getSequence(crypto_text,4)

    seq5 = getSequence(crypto_text,5)

    list_of_seqs = []

    list_of_seqs.append(seq1)
    list_of_seqs.append(seq2)
    list_of_seqs.append(seq3)
    list_of_seqs.append(seq4)
    list_of_seqs.append(seq5)



    for i in range(len(list_of_seqs)):
        print(f'for key length = {i+1}\n')

        for j in range(len(list_of_seqs[i])):

            print(f'sequence {j+1}: {list_of_seqs[i][j]} IC = {getCindex(list_of_seqs[i][j])}\n')


if __name__ == "__main__":
    main(sys.argv)
