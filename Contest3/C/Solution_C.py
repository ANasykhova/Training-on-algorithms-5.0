number = int(input())
a = map(int, input().split())

counts = [0] * (100003)
for el in a:
    counts[el + 1] += 1

max_ = 0
total_count = 0
for i in range(1, 100002):
    left = counts[i - 1]
    curr = counts[i]
    right = counts[i + 1]
    total_count += curr
    sum_l = left + curr
    sum_r = curr + right
    if sum_l > max_:
        max_ = sum_l
    if sum_r > max_:
        max_ = sum_r

print(total_count - max_)
