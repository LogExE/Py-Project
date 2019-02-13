#Brown–Robinson method
from collections import Counter
def max_by_sec(arr):
    return max(enumerate(arr), key = lambda x: x[1])
def min_by_sec(arr):
    return min(enumerate(arr), key = lambda x: x[1])
def sum_iter(*arr):
    return tuple(map(sum, zip(*arr)))

n, m, it, cur_st = int(input("N: ")), int(input("M: ")),\
           int(input("Number of iterations: ")),\
           int(input("Number of first strategy: ")) - 1
print("Matrix:")
mat = tuple(tuple(map(int, input().split(' ', m))) for i in range(n))
trmat = tuple(zip(*mat))
Vmean = None
addA = [0] * n
addB = [0] * m
used_st_A = [0] * it
used_st_B = [0] * it
for i in range(it):
    taddA = addA[:]
    addA = sum_iter(mat[cur_st], addA)
    cur_arrA = sum_iter(mat[cur_st], taddA)
    j, Vmin = min_by_sec(cur_arrA)
    taddB = addB[:]
    addB = sum_iter(trmat[j], addB)
    cur_arrB = sum_iter(trmat[j], taddB)
    nexti, Vmax = max_by_sec(cur_arrB)
    Vmean = (Vmin + Vmax) / (2 * i + 2)
    used_st_A[i] = cur_st
    used_st_B[i] = j
    cur_st = nexti
cA = Counter(used_st_A)
cB = Counter(used_st_B)
print("I frequences:")
for i in range(n):
    print(i + 1, cA[i] / it)
print("II frequences:")
for i in range(m):
    print(i + 1, cB[i] / it)
print("Price:")
print(Vmean)
