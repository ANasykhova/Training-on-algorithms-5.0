races, classes = map(int, input().split())
table = []
for i in range(races):
    table.append(list(map(int, input().split())))


def find_max(banned_row, banned_col):
    answer = 0
    row = col = 0
    for i in range(races):
        if i != banned_row:
            for j in range(classes):
                if j != banned_col and table[i][j] > answer:
                    answer = table[i][j]
                    row = i
                    col = j

    return row, col, answer


max_r, max_c, max_val = find_max(-1, -1)

_, ban_col, _ = find_max(max_r, -1)
_, _, ban_row_val = find_max(max_r, ban_col)

ban_row, _, _ = find_max(-1, max_c)
_, _, ban_col_val = find_max(ban_row, max_c)

if ban_row_val < ban_col_val:
    print(max_r + 1, ban_col + 1)
else:
    print(ban_row + 1, max_c + 1)
