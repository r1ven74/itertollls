from itertools import permutations
r1 = ['Р1']
r2 = ['Р2']
r3= ['Р3']
r4 = ["Р4"]
r5 = ['Р5']
r6 = ['Р6']
r7= ['Р7']
vsego = r1 + r2 + r3+r4+r5+r6+r7
unique_permutations = set(permutations(vsego, 2))
print(unique_permutations)