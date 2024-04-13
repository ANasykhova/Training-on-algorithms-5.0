points = int(input())
coords = []
for i in range(points):
    coords.append(tuple(map(int, input().split())))

coords_set = set(coords)
x0, y0 = coords[0]
answer = [(x0 + 1, y0 + 1), (x0 + 1, y0), (x0, y0 + 1)]
length = 3

for i in range(points):
    for j in range(points):
        if i != j:
            x1, y1 = coords[i]
            x2, y2 = coords[j]

            dx = x2 - x1
            dy = y2 - y1

            x3 = x1 + dy
            y3 = y1 - dx

            xy3 = (x3, y3)
            xy4 = (x3 + dx, y3 + dy)

            if xy3 in coords_set and xy4 in coords_set:
                answer = []
                length = 0

            if length > 1 and xy3 in coords_set:
                answer = [xy4]
                length = 1

            if length > 1 and xy4 in coords_set:
                answer = [xy3]
                length = 1

            if length > 2:
                answer = [xy3, xy4]
                length = 2

print(length)
for now in answer:
    print(*now)
