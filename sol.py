n, m = int(input("N:")), int(input("M:"))
mat = [list(map(int, input().split(' ', m))) for i in range(n)]
minAs = set()
for arr in mat:
    minAs.add(min(arr))
maxmin = max(minAs)
maxBs = set()
for arr in zip(*mat):
    maxBs.add(max(arr))
minmax = min(maxBs)
print(f"maxmin: {maxmin}, minmax: {minmax}")
print("Опорная точка есть" if minmax == maxmin else "Опорной точки нет")