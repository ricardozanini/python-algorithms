def can_be_extended_to_solution(perm):
    i = len(perm) - 1
    for j in range(i):
        if i - j == abs(perm[i] - perm[j]):
            return False
    return True

def extend(perm, n):
    if len(perm) == n:
        global SOLUTIONS
        print(perm)
        SOLUTIONS += 1
        #exit()# this exit only finds one solution if uncommented

    for k in range(n):
        if k not in perm:
            perm.append(k)

            if can_be_extended_to_solution(perm):
                extend(perm, n)

            perm.pop()

SOLUTIONS = 0
extend(perm = [], n = 8)
print("Number of solutions %s" % SOLUTIONS)