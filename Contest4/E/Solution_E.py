n = int(input())

left, right = 1, n
while left < right:
    middle = (left + right) // 2
    if (1 + middle) * middle // 2 >= n:
        right = middle
    else:
        left = middle + 1

sum_ = (1 + left) * left // 2
diff = sum_ - n
if left % 2 == 0:
    numerator = 1 + diff
    denominator = left - diff
else:
    numerator = left - diff
    denominator = 1 + diff

print(f'{numerator}/{denominator}')
