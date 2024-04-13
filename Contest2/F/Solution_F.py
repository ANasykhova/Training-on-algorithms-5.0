number = int(input())
sectors = list(map(int, input().split()))
a, b, diff = map(int, input().split())

start = (a - 1) // diff
end = min(number, (b - 1) // diff + 1 - start)

max_sector = 0

for i in [-1, 1]:
    index = ((i * start) % number + number) % number
    for j in range(end):
        if sectors[index] > max_sector:
            max_sector = sectors[index]
        index += i
        index = (index % number + number) % number

print(max_sector)
