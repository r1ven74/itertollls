from itertools import permutations

apple = ['З'] * 2
grusha = ['С'] * 3
orange = ['К'] * 4
beads = apple + grusha + orange
unique_permutations = set(permutations(beads))
print(unique_permutations)