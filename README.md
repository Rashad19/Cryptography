# Cryptography



### Index of Coincidence Attack

`Cindex.py` implements a method for calculating the Index of Coincidence (I.C) of Cryptotext for the Vignere cipher of different key lengths
The purpose of this attack is to determine the most likely key length.

The formula to calculate I.C is shown below:

- where f_i is the absolute frequency of each letter of the alphabet
- N is the total length of the cryptotext
- k is the number letters in the alphabet in question.

$$\large I.C = \frac{\sum\limits^{k}_{i=0} f_i(f_i - 1)}{N(N-1)}$$

We want to generate sequences of cryptotext letters which were encrypted by the same ki in key = [k1, k2, ...., kn] of length n.

for key lengths (n) = 

1: We calculate I.C value for 1 sequence (The Whole cryptotext)

2: We want to 2 sequences whith letters encrypted by the same ki and we calculate the average I.C value between the two

.
.
.
.

n: We want to n sequences with letters encrypted by the same ki and we calculate the average I.C value between them

### Frequency Analysis

`FreqAnalysis.py` performs a frequency attack on the Shift and multiplicative cipher.



