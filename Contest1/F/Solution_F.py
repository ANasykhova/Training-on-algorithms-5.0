number = int(input())
a = list(map(int, input().split()))

flag = a[0] % 2 != 0

for i in range(1, number):
    if flag:
        if a[i] % 2 != 0:
            print(chr(120), end='')
        else:
            print('+', end='')
    else:
        if a[i] % 2 != 0:
            print('+', end='')
            flag = True
        else:
            print(chr(120), end='')
