def can_be_extended_to_solution(perm):
    i = len(perm) - 1
    for j in range(i):
        if i - j == abs(perm[i] - perm[j]):
            return False
    return True

def extend(perm, n,total):
    if len(perm) == n:
        print(perm)
        total.append(perm)

    for k in range(n):
        if k not in perm:
            perm.append(k)

            if can_be_extended_to_solution(perm):
                extend(perm, n, total)

            perm.pop()
total_var = []
extend(perm = [], n = 8,total =total_var)
print(len(total_var))
