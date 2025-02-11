from itertools import permutations
emerald = ['б'] * 5
rubin = ['по'] * 6
sapfhire = ['с'] * 7
vsego = emerald + rubin + sapfhire
unique_permutations = set(permutations(vsego))
print(unique_permutations)
