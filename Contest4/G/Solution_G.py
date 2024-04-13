n, m = map(int, input().split())
prefix = [[0] * (m + 1)]
for i in range(n):
    prefix.append([0] * (m + 1))
    s = '.' + input()
    for j in range(1, m + 1):
        prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]
        if s[j] == '#':
            prefix[i][j] += 1


def is_square(i, j, k):
    return prefix[i][j] - prefix[i - k][j] - prefix[i][j - k] + prefix[i - k][j - k] == k ** 2


def check(k):
    for i in range(1, n - 2 * k + 1):
        for j in range(1, m - 2 * k + 1):
            if is_square(i, j + k, k) and \
                    is_square(i + k, j, k) and \
                    is_square(i + k, j + k, k) and \
                    is_square(i + k, j + 2 * k, k) and \
                    is_square(i + 2 * k, j + k, k):
                return True
    return False


left, right = 1, n
while left < right:
    middle = (left + right + 1) // 2
    if check(middle):
        left = middle
    else:
        right = middle - 1
print(left)
