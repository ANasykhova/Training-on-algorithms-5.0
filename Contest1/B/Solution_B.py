first_1, first_2 = map(int, input().split(':'))
second_1, second_2 = map(int, input().split(':'))
place = int(input())

diff = first_2 - first_1 + second_2 - second_1
if diff < 0:
    print(0)
else:
    if (place == 1 and second_1 + diff <= first_2) or (place == 2 and first_1 <= second_2):
        print(diff + 1)
    else:
        print(diff)
