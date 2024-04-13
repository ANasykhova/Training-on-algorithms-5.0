def find_len(k):
    temp = ((1 + k) * k) // 2
    spaces = max(temp - 1, 0)
    return spaces + temp * k - temp * (2 * k + 1) // 3 + temp


max_length = int(input())
left, right = 0, max_length + 1
while left < right:
    middle = (left + right + 1) // 2
    if find_len(middle) <= max_length:
        left = middle
    else:
        right = middle - 1
print(left)
