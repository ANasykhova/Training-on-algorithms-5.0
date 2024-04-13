test_count = int(input())

for i in range(test_count):
    length = int(input())
    a = list(map(int, input().split()))
    i = 0
    curr_min = a[0]
    answer = []
    test = []
    while i < length:
        if curr_min >= len(test) + 1 and a[i] >= len(test) + 1:
            test.append(a[i])
            if a[i] < curr_min:
                curr_min = a[i]
            i += 1
        else:
            answer.append(len(test))
            test = []
            curr_min = a[i]
    answer.append(len(test))

    print(len(answer))
    print(*answer, sep=' ')
