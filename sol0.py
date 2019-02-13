n, m = int(input("N: ")), int(input("M: "))
print("Matrix:")
mat = tuple(list(map(int, input().split(' ', m))) for i in range(n))
minAs = tuple(min(enumerate(arr), key = lambda x: x[1]) for arr in mat)
maxmin = max(minAs, key = lambda x: x[1])
# zip(*mat) - transposed matrix
# lambda x: x[1] - returns the second element of iterable
maxBs = tuple(max(enumerate(arr), key = lambda x: x[1]) for arr in zip(*mat))
minmax = min(maxBs, key = lambda x: x[1])
print(f"maxmin: {maxmin[1]}, minmax: {minmax[1]}")
if minmax[1] == maxmin[1]:
    print(f"Saddle point exists, price of game is {minmax[1]}")
    print(f"Numbers of pure strategys I: {minmax[0] + 1}, II: {maxmin[0] + 1}")
else:
    print("No saddle point.")
