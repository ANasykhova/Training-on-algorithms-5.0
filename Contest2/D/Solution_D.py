n = int(input())
board = []
for i in range(10):
    board.append([0] * 10)

for i in range(n):
    x, y = map(int, input().split())
    board[x][y] = 1

perimeter = 0
for i in range(1, 9):
    for j in range(1, 9):
        if board[i][j] == 1:
            dx = [-1, 0, 1, 0]
            dy = [0, -1, 0, 1]
            for k in range(4):
                if board[i + dx[k]][j + dy[k]] == 0:
                    perimeter += 1

print(perimeter)
