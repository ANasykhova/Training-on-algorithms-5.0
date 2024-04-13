def calc(t, our, health, prod):
    count = 0
    their = 0

    if health >= t:
        if prod >= our:
            return 1e9

        health -= our
        if health >= 0:
            their += prod

        count += 1

        if health >= t:
            count += (health - t) // (our - prod)
            health -= count * (our - prod)
            their = 0

            if health >= 0:
                their += prod

            count += 1

    while health > 0:
        if our <= 0:
            return 1e9
        if health >= our:
            health -= our
        else:
            their -= our - health
            health = 0
        our -= their
        if health > 0:
            their += prod
        count += 1

    while their > 0:
        if our <= 0:
            return 1e9
        their -= our
        if their > 0:
            our -= their
        count += 1

    return count


our = int(input())
health = int(input())
prod = int(input())

result = 1e9
for t in range(health + 2):
    result = min(result, calc(t, our, health, prod))

if result == 1e9:
    print(-1)
else:
    print(result)
