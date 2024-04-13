total = {}


def add_to_dict(arr):
    for el in arr:
        if el in total:
            total[el] += 1
        else:
            total[el] = 1


_ = int(input())
first = list(map(int, input().split()))
add_to_dict(set(first))

_ = int(input())
second = list(map(int, input().split()))
add_to_dict(set(second))

_ = int(input())
third = list(map(int, input().split()))
add_to_dict(set(third))

for number, count in sorted(total.items()):
    if count >= 2:
        print(number, end=' ')
