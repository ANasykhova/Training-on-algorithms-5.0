width, height, tiles = map(int, input().split())

coords = []
for i in range(tiles):
    coords.append(tuple(map(int, input().split())))
coords.sort()
x, y = [], []
for x_i, y_i in coords:
    x.append(x_i)
    y.append(y_i)

prefmin = [y[0]] * tiles
prefmax = [y[0]] * tiles
sufmin = [y[-1]] * tiles
sufmax = [y[-1]] * tiles

for i in range(1, tiles):
    prefmin[i] = min(prefmin[i - 1], y[i])
    prefmax[i] = max(prefmax[i - 1], y[i])

for i in range(tiles - 2, -1, -1):
    sufmin[i] = min(sufmin[i + 1], y[i])
    sufmax[i] = max(sufmax[i + 1], y[i])


def check(target):
    r = 0
    pmx = - 1e9
    pmn = 1e9

    for i in range(tiles):
        while r < tiles and x[r] < x[i] + target:
            r += 1
        mx = pmx
        mn = pmn
        if r != tiles:
            mx = max(mx, sufmax[r])
            mn = min(mn, sufmin[r])

        if mx - mn < target:
            return True
        pmx = prefmax[i]
        pmn = prefmin[i]
    return False


left, right = 1, min(width, height)
while left < right:
    middle = (left + right) // 2
    if check(middle):
        right = middle
    else:
        left = middle + 1

print(left)
