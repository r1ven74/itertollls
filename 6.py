from itertools import permutations
astra = ['А']
vega = ['В']
grif = ['Г']
vsego = astra + vega + grif
unique_permutations = set(permutations(vsego, 2))
print(unique_permutations)
