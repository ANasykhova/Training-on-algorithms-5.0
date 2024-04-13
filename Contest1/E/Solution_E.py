start, founders, days = map(int, input().split())
start *= 10
for i in range(10):
    if (start + i) % founders == 0:
        start += i
        print(str(start) + "0" * (days - 1))
        break
else:
    print(-1)
