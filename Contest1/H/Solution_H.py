def check(length, x1, speed_1, x2, speed_2):
    time = 1000000000
    if x1 == x2 or (x1 + x2) % length == 0:
        print('YES')
        print(0)
        return

    diff = speed_1 - speed_2
    sum_ = speed_1 + speed_2

    if diff > 0:
        k = (x1 - x2) // length + 1
        time = 1.0 * (k * length - x1 + x2) / diff
    if diff < 0:
        k = (x1 - x2) // length
        time = 1.0 * (k * length - x1 + x2) / diff

    if sum_ > 0:
        k = (x1 + x2) // length + 1

        if 1.0 * (k * length - x1 - x2) / sum_ < time:
            time = 1.0 * (k * length - x1 - x2) / sum_

    if sum_ < 0:
        k = (x1 + x2) // length

        if 1.0 * (k * length - x1 - x2) / sum_ < time:
            time = 1.0 * (k * length - x1 - x2) / sum_

    if time == 1000000000:
        print('NO')
    else:
        print('YES')
        print(time)


length, x1, speed_1, x2, speed_2 = map(int, input().split())
check(length, x1, speed_1, x2, speed_2)
