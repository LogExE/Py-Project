n, m = int(input("N: ")), int(input("M: "))
print("Matrix:")
mat = tuple(list(map(int, input().split(' ', n))) for i in range(m))
minAs = tuple(min(enumerate(arr), key = lambda x: x[1]) for arr in mat)
maxmin = max(minAs, key = lambda x: x[1])
# zip(*mat) - transposed matrix
# lambda x: x[1] - returns the second element of pair
maxBs = tuple(max(enumerate(arr), key = lambda x: x[1]) for arr in zip(*mat))
minmax = min(maxBs, key = lambda x: x[1])
print(f"maxmin: {maxmin[1]}, minmax: {minmax[1]}")
if minmax[1] == maxmin[1]:
    print(f"Saddle point exists, price of game is {minmax[1]}")
    print(f"Numbers of pure strategys I: {minmax[0] + 1}, II: {maxmin[0] + 1}")
else:
    print("No saddle point.")
    if n == m and n == 2:
        den = mat[0][0] + mat[1][1] - mat[0][1] - mat[1][0]
        print(f"p1* = {(mat[1][1] - mat[1][0]) / den}, p2* = {(mat[0][0] - mat[0][1]) / den}")
        print(f"q1* = {(mat[1][1] - mat[0][1]) / den}, q2* = {(mat[0][0] - mat[1][0]) / den}")
        print(f"{chr(0x3BD)} = {(mat[1][1] * mat[0][0] - mat[0][1] * mat[1][0]) / den}")
