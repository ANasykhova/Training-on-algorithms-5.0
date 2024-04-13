n = int(input())
length = list(map(int, input().split()))

max_ = length[0]
sum_ = 0
for len_i in length:
    if len_i > max_:
        max_ = len_i
    sum_ += len_i

if sum_ - max_ < max_:
    print(2 * max_ - sum_)
else:
    print(sum_)
