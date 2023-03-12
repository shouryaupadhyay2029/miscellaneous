import pandas as pd
import numpy as np

A = 'A'
T = 'T'
G = 'G'
C = 'c'

dna_human_one = [A,T,G,T,G,T,G,G,C,A,T,T,T,G,G,G,C,G,C,T,G,T,T,T,G,G,C,A,G,T,A,T,G,A,T,T,G,C,C,T,T,T,C,T]
dna_human_two = [A,T,G,T,G,T,G,G,C,A,T,T,T,G,G,G,C,G,C,T,G,T,T,T,G,G,C,A,G,T,A,T,G,A,T,T,G,C,T,T,T,T,C,T]

match = 0
varation = 0

for x in range(len(dna_human_one)):
    if dna_human_one[x] == dna_human_two[x]:
        match += 1
    else:
        varation += 1

x = (match-varation)/44
y = (varation)/44
print('DATA has MATCHED > ',x*100,'%')
print('VARATION>',y*100,'%')


