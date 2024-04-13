number = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
numbers.append(1e9 + 1)


def lbinsearch(value):
    left, right = 0, number
    while left < right:
        middle = (left + right) // 2
        if numbers[middle] >= value:
            right = middle
        else:
            left = middle + 1
    return left


query = int(input())
for i in range(query):
    l, r = map(int, input().split())
    count = lbinsearch(r + 1) - lbinsearch(l)
    print(count, end=' ')
