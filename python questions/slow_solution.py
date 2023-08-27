t = int(input())
for i in range(t):
    maxt, maxn, sumn = map(int, input().split())

    ans = 0

    while maxt and sumn:
        n = min(maxn, sumn)
        ans += n**2

        maxt -= 1
        sumn -= n

    print(ans)
