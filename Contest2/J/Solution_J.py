n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(input()))


def is_rect(fi, fj, ti, tj, filler):
    min_i = min_j = 201
    max_i = max_j = -1
    count = 0

    for i in range(fi, ti):
        for j in range(fj, tj):
            if board[i][j] != '.':
                if i < min_i:
                    min_i = i
                if j < min_j:
                    min_j = j

                if i > max_i:
                    max_i = i
                if j > max_j:
                    max_j = j

                board[i][j] = filler
                count += 1
    return count > 0 and (max_i - min_i + 1) * (max_j - min_j + 1) == count


def print_answer():
    print('YES')
    for row in board:
        print(''.join(row))


def solve():
    for i in range(n):
        if is_rect(0, 0, i, m, 'a') and is_rect(i, 0, n, m, 'b'):
            print_answer()
            return

    for j in range(m):
        if is_rect(0, 0, n, j, 'a') and is_rect(0, j, n, m, 'b'):
            print_answer()
            return

    print('NO')
    return


solve()
