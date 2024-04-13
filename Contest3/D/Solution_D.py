days, dist = map(int, input().split())
indications = list(map(int, input().split()))
ind_dict = {}
flag = False
for i in range(days):
    if indications[i] in ind_dict and i - ind_dict[indications[i]] <= dist:
        flag = True
        break
    else:
        ind_dict[indications[i]] = i

if flag == True:
    print('YES')
else:
    print('NO')
