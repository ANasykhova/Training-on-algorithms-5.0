regiments, sorties = map(int, input().split())
orcs = [0] + list(map(int, input().split()))

pref_sum = [0] * (regiments + 1)
for i in range(1, regiments + 1):
    pref_sum[i] = pref_sum[i - 1] + orcs[i]

for i in range(sorties):
    reg_count, orc_per_sortie = map(int, input().split())
    left, right = 1, regiments + 1 - reg_count
    while left < right:
        middle = (left + right) // 2
        if pref_sum[middle + reg_count - 1] - pref_sum[middle - 1] >= orc_per_sortie:
            right = middle
        else:
            left = middle + 1

    if pref_sum[left + reg_count - 1] - pref_sum[left - 1] == orc_per_sortie:
        print(left)
    else:
        print(-1)
