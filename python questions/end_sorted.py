for t in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))

    cnt_1, cnt_n = 0,0

    index_1 = p.index(1)
    index_n = p.index(n)

    cnt_1 = abs(0 - index_1)
    cnt_n = abs((n-1) - index_n)

    if index_1 > index_n:
        print(cnt_1 + cnt_n - 1)
    else:
        print(cnt_1 + cnt_n)
