# Cryptography



### Index of Coincidence Attack

`Cindex.py` implements a method for calculating the Index of Coincidence (I.C) of Cryptotext for the Vignere cipher of different key lengths
The purpose of this attack is to determine the most likely key length.

The formula to calculate I.C is shown below:

- where f_i is the absolute frequency of each letter of the alphabet
- N is the total length of the cryptotext

![Dark](https://latex.codecogs.com/svg.image?\mathbf{\color{white}&space;I.C&space;=\frac{\sum_{i=1}^{k}&space;f_{i}(f_{i}-1)}{N(N-1)}#gh-dark-mode-only)
![light](https://latex.codecogs.com/svg.image?\mathbf{\color{black}&space;I.C&space;=\frac{\sum_{i=1}^{k}&space;f_{i}(f_{i}-1)}{N(N-1)}#gh-light-mode-only)


### Frequency Analysis

`FreqAnalysis.py` performs a frequency attack on the Shift and multiplicative cipher.



