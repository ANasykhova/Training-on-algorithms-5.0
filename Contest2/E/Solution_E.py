def solve():
    berries = int(input())
    max_up = [0, 0, 0]
    max_down = [0, 0, 0]

    result_up = []
    result_down = []

    max_height = 0

    for i in range(berries):
        up, down = map(int, input().split())
        if up > down:
            if down > max_up[1]:
                max_up = [up, down, i + 1]
            max_height += up - down
            result_up.append(i + 1)
        else:
            if up > max_down[0]:
                max_down = [up, down, i + 1]
            result_down.append(i + 1)

    max_height += max_up[1] - max_up[0]

    if max_up[2] not in result_up:
        result_down.remove(max_down[2])
        max_height += max_down[0]
        print(max_height)
        print(max_down[2], end=' ')
        print(*result_down, sep=' ', end=' ')
        return

    if max_down[2] not in result_down:
        result_up.remove(max_up[2])
        max_height += max_up[0]
        print(max_height)
        print(*result_up, sep=' ', end=' ')
        print(max_up[2], end=' ')
        return

    result_up.remove(max_up[2])
    result_down.remove(max_down[2])

    maxes = [0] * 4

    maxes[0] = max_height + max_up[0]
    maxes[1] = max_height + max_up[0] - max_up[1] + max_down[0]
    maxes[2] = max_height + max_down[0]
    maxes[3] = max_height + max_up[0] - max_down[1] + max_down[0]

    max_height = maxes[0]
    index = 0
    for i in range(1, 4):
        if maxes[i] > max_height:
            max_height = maxes[i]
            index = i

    print(max_height)
    if index in [0, 1]:
        print(*result_up, sep=' ', end=' ')
        print(max_up[2], end=' ')
        print(max_down[2], end=' ')
        print(*result_down, sep=' ', end=' ')

    else:
        print(*result_up, sep=' ', end=' ')
        print(max_down[2], end=' ')
        print(max_up[2], end=' ')
        print(*result_down, sep=' ', end=' ')


solve()
