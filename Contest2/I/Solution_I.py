def median(lst):
    lst.sort()
    n = len(lst)
    if n % 2 == 0:
        return (lst[n // 2 - 1] + lst[n // 2]) / 2
    else:
        return lst[n // 2]


ship = int(input())
answer = 0
ships = []
y_lst = []
for i in range(ship):
    x, y = map(int, input().split())
    ships.append((x, y))
    y_lst.append(y)

med_y = int(median(y_lst))
i = 1
for x, y in sorted(ships):
    answer += abs(i - x)
    answer += abs(med_y - y)
    i += 1

print(answer)
