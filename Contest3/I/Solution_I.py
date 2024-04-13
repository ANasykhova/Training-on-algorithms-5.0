lines = (open("input.txt", "r").read()).split('\n')
length = len(lines)
if lines[length - 1] == '':
    length -= 1
total_goals = {}
open_games = {}
count_games = {}
players_teams = {}
times = {}


def update_goals(dictionary, name, score):
    dictionary[name] = dictionary.get(name, 0) + score


def update_times(name, time):
    if name in times:
        times[name].append(time)
    else:
        times[name] = [time]


def get_match_info(start):
    spl = lines[start].split(' - ')
    team1 = spl[0]
    team2 = ' '.join(spl[1].split()[:-1])
    score = spl[1].split()[-1]

    first, second = map(int, score.split(':'))

    update_goals(count_games, team1, 1)
    update_goals(count_games, team2, 1)
    update_goals(total_goals, team1, first)
    update_goals(total_goals, team2, second)

    if first + second != 0:

        open1 = int(lines[start + 1].split()[-1][:-1]) if first != 0 else 91
        open2 = int(lines[start + first + 1].split()[-1][:-1]) if second != 0 else 91

        if open1 < open2:
            player1 = ' '.join(lines[start + 1].split()[:-1])
            update_goals(open_games, team1, 1)
            update_goals(open_games, player1, 1)
        else:
            player2 = ' '.join(lines[start + 1 + first].split()[:-1])
            update_goals(open_games, team2, 1)
            update_goals(open_games, player2, 1)

        for i in range(start + 1, start + first + 1):
            spl = lines[i].split()
            time = int(spl[-1][:-1])
            name = ' '.join(spl[:-1])

            players_teams[name] = team1

            update_times(name, time)
            update_goals(total_goals, name, 1)

        for i in range(start + first + 1, start + first + second + 1):
            spl = lines[i].split()
            time = int(spl[-1][:-1])
            name = ' '.join(spl[:-1])

            players_teams[name] = team2

            update_times(name, time)
            update_goals(total_goals, name, 1)

    return start + first + second + 1


def answer_query(idx):
    query = lines[idx].split()
    if query[0] == 'Total':
        name = ' '.join(query[3:])
        return total_goals.get(name, 0)

    elif query[0] == 'Mean':
        name = ' '.join(query[5:])
        if name in total_goals:
            team = players_teams.get(name, False)
            if team:
                count = count_games[team]
            else:
                count = count_games[name]

            return total_goals[name] / count

    elif query[0] == 'Score':
        name = ' '.join(query[3:])
        return open_games.get(name, 0)

    elif query[0] == 'Goals':
        time = int(query[3])
        if query[2] == 'last':
            name = ' '.join(query[6:])
            curr_times = times.get(name, [])
            return sum(el >= 91 - time for el in curr_times)

        if query[2] == 'first':
            name = ' '.join(query[6:])
            curr_times = times.get(name, [])
            return sum(el <= time for el in curr_times)

        if query[2] == 'minute':
            name = ' '.join(query[5:])
            return times.get(name, []).count(time)

    return 0


result = []
end = 0
while end < length and lines[end][0] != '"':
    result.append(0)
    end += 1
while end < length:
    if lines[end][0] == '"':
        end = get_match_info(end)
        while end < length and lines[end][0] != '"':
            result.append(answer_query(end))
            end += 1

res = open("output.txt", "w").write('\n'.join(map(str, result)))
