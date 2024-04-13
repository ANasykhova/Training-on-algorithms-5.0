def get_diff():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1, y1) > (x2, y2):
        x1, y1, x2, y2 = x2, y2, x1, y1
    return (x2 - x1, y2 - y1), x1, y1


matches = int(input())
bytype = {}
for i in range(matches):
    diff, x1, y1 = get_diff()
    if diff not in bytype:
        bytype[diff] = []
    bytype[diff].append((x1, y1))

mxmy = {}
for i in range(matches):
    diff, x1, y1 = get_diff()

    for xp, yp in bytype.get(diff, []):
        m = (x1 - xp, y1 - yp)
        mxmy[m] = mxmy.get(m, 0) + 1

max_inplace = 0
for coords in mxmy:
    if mxmy[coords] > max_inplace:
        max_inplace = mxmy[coords]

print(matches - max_inplace)
