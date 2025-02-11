from itertools import permutations
red_flags = ['к'] * 4
blue_flags = ['с'] * 4 #считаем кол-во красных, желтых и голубых флажков
yellow_flags = ['ж'] * 8
flags = red_flags + blue_flags + yellow_flags #складываем кол-во всех флажков
unique_permutations = set(permutations(flags))
print(unique_permutations)
