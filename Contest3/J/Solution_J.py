n, k = map(int, input().split())

parts = []  # flag for each device that part downloaded
priority = []  # for each device priority index of other devices
downloaded = []  # for each device total count of parts downloaded
for i in range(n):
    parts.append([False] * k)
    priority.append([0] * n)
    downloaded.append(0)

parts[0] = [True] * k
downloaded[0] = k
ans = [0] * n

cntparts = [1] * k  # for each part find count of devices
total_parts = k
iteration = 0

while total_parts != n * k:
    iteration += 1

    # determinate on how many devices this part is downloaded
    sorted_cntparts = []
    for i in range(k):
        sorted_cntparts.append((cntparts[i], i))
    sorted_cntparts.sort()

    # find necessary part to load for each device
    wanted_part = [-1] * n
    for partindex in range(k):
        nowpart = sorted_cntparts[partindex][1]
        for i in range(n):
            if not parts[i][nowpart] and wanted_part[i] == -1:
                wanted_part[i] = nowpart

    # choose device from which to load part
    choosereq = [(0, k + 1)] * n
    for i in range(n):
        if wanted_part[i] != -1:
            for j in range(n):
                if parts[j][wanted_part[i]] and downloaded[j] < choosereq[i][1]:
                    choosereq[i] = (j, downloaded[j])

    # send requests
    requests = []
    for i in range(n):
        requests.append([])
    for i in range(n):
        if wanted_part[i] != -1:
            fr = choosereq[i][0]
            requests[fr].append((priority[fr][i], downloaded[i], wanted_part[i], i))
    for i in range(n):
        requests[i].sort(key=lambda x: (-x[0], x[1], x[3]))

    # handle requests
    for i in range(n):
        if len(requests[i]) > 0:
            fr = i
            to = requests[i][0][3]
            part = requests[i][0][2]

            parts[to][part] = True
            cntparts[part] += 1
            downloaded[to] += 1
            total_parts += 1
            priority[to][fr] += 1

            if downloaded[to] == k:
                ans[to] = iteration

print(*ans[1:])
