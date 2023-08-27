for t in range(int(input())):
    e,k = map(int, input().split())

    count = 0

    while e>0:
        n = (e//k)
        count += 1
        e = n

    print(count)
