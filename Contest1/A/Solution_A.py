vasya, v = map(int, input().split())
masha, m = map(int, input().split())

vasya_left, vasya_right = vasya - v, vasya + v
masha_left, masha_right = masha - m, masha + m

min_left = min(vasya_left, masha_left)
max_right = max(vasya_right, masha_right)

if abs(masha - vasya) <= v + m:
    print(max_right - min_left + 1)
else:
    between = abs(masha - vasya) - v - m - 1
    print(max_right - min_left + 1 - between)
