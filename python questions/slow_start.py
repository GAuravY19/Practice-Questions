for _ in range(int(input())):
    x,y = map(int, input().split())

    count = 0
    i = 0
    damage = 0

    while(damage < y):
        if i < 5:
            damage += x//2
            count += 1
        else:
            damage += x
            count += 1

        i += 1

    print(count)
