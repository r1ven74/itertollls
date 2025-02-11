from itertools import permutations
bandit = ['б'] * 2
police = ['по'] * 2 #считаем кол-во всех друзей
sishik = ['с']
prohojiy = ["пр"] * 5
vsego = bandit + police + sishik + prohojiy #складываем кол-во всех друзей
unique_permutations = set(permutations(vsego))
print(unique_permutations)
