import itertools as it

def is_solution(perm):
    for (i1, i2) in it.combinations(range(len(perm)), 2):
        if abs(i1 - i2) == abs(perm[i1] - perm[i2]):
            return False

    return True
size = int(input("how large is the board"))
for perm in it.permutations(range(size)):
    if is_solution(perm):
        print(perm)
        exit()
