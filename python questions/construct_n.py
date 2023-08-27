for _ in range(int(input())):
    n = int(input())

    count = False

    for i in range(n):
        for j in range(n):
            if 2 * i + 7 * j == n:
                count = True

    if count :
        print('YES')
    else:
        print('NO')
