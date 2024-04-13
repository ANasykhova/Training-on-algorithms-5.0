days, diff = map(int, input().split())
prices = list(map(int, input().split()))

max_profit = 0
for i in range(days):
    max_for_i = prices[i]

    end = min(i + diff + 1, days)

    for j in range(i + 1, end):
        if prices[j] > max_for_i:
            max_for_i = prices[j]

    profit = max_for_i - prices[i]
    if profit > max_profit:
        max_profit = profit

print(max_profit)
