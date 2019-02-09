n, m = int(input("N: ")), int(input("M: "))
print("Матрица:")
mat = tuple(list(map(int, input().split(' ', n))) for i in range(m))
minAs = tuple(min(enumerate(arr), key = lambda x: x[1]) for arr in mat)
maxmin = max(minAs, key = lambda x: x[1])
# zip(*mat) - транспонированная исходная матрица
# lambda x: x[1] - возращает второй элемент пары
maxBs = tuple(max(enumerate(arr), key = lambda x: x[1]) for arr in zip(*mat))
minmax = min(maxBs, key = lambda x: x[1])
print(f"maxmin: {maxmin[1]}, minmax: {minmax[1]}")
if minmax[1] == maxmin[1]:
    print(f"Есть седловая точка, цена игры: {minmax[1]}")
    print(f"Номер чистых cтратегий I: {minmax[0] + 1}, II: {maxmin[0] + 1}")
else:
    print("Седловой точки нет.")
