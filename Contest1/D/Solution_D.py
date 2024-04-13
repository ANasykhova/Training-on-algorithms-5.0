board = []
pos = []
for i in range(8):
    board.append([0] * 8)
    curr = input()
    for j in range(8):
        if curr[j] != '*':
            pos.append((curr[j], i, j))
            board[i][j] = 2

for symbol, x, y in pos:
    if symbol == 'R':
        i = 1
        while x - i > -1 and board[x - i][y] != 2:
            board[x - i][y] = 1
            i += 1

        i = 1
        while x + i < 8 and board[x + i][y] != 2:
            board[x + i][y] = 1
            i += 1

        i = 1
        while y - i > -1 and board[x][y - i] != 2:
            board[x][y - i] = 1
            i += 1

        i = 1
        while y + i < 8 and board[x][y + i] != 2:
            board[x][y + i] = 1
            i += 1

    if symbol == 'B':
        i = 1
        while x + i < 8 and y + i < 8 and board[x + i][y + i] != 2:
            board[x + i][y + i] = 1
            i += 1

        i = 1
        while x + i < 8 and y - i > -1 and board[x + i][y - i] != 2:
            board[x + i][y - i] = 1
            i += 1

        i = 1
        while x - i > -1 and y + i < 8 and board[x - i][y + i] != 2:
            board[x - i][y + i] = 1
            i += 1

        i = 1
        while x - i > -1 and y - i > -1 and board[x - i][y - i] != 2:
            board[x - i][y - i] = 1
            i += 1

count = 0
for i in board:
    count += i.count(0)

print(count)
