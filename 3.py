
from itertools import permutations

green_beads = ['З'] * 4
blue_beads = ['С'] * 5
red_beads = ['К'] * 6
beads = green_beads + blue_beads + red_beads
unique_permutations = set(permutations(beads))
print(unique_permutations)