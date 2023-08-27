t = int(input())
for i in range(t):
    w1,w2,x1,x2,m = map(int, input().split())
    diff = w2-w1
    lim1 = x1 * m
    lim2 = x2 * m

    if lim1 <= diff and diff <= lim2:
        print(1)
    else:
        print(0)
