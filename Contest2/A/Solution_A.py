number = int(input())
left_x, left_y = 1e9 + 1, 1e9 + 1
right_x, right_y = 0, 0
while number > 0:
    x, y = map(int, input().split())
    left_x = min(x, left_x)
    left_y = min(y, left_y)
    right_x = max(x, right_x)
    right_y = max(y, right_y)
    number -= 1

print(left_x, left_y, right_x, right_y)
