rows = int(input())
clicks = 0
for i in range(rows):
    spaces = int(input())
    clicks += spaces // 4
    spaces %= 4
    if spaces == 1:
        clicks += 1
    if spaces == 2 or spaces == 3:
        clicks += 2

print(clicks)
