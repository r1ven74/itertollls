from itertools import permutations
r1 = ['Р1']
r2 = ['Р2']
r3= ['Р3']
r4 = ["Р4"]
vsego = r1 + r2 + r3+r4
unique_permutations = set(permutations(vsego, 3))
print(unique_permutations)