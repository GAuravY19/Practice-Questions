t = int(input())
for i in range(t):
    n = int(input())
    o = list(map(int, input().split()))
    a = list(map(int, input().split()))

    count_o = 0
    count_a = 0
    count_om = []
    count_andy = []

    for j in range(n):
        if o[j] != 0:
            count_o += 1
            count_om.append(count_o)
        else:
            count_o = 0

    for j in range(0,n):
        if a[j] != 0:
            count_a += 1
            count_andy.append(count_a)

        else:
            count_a = 0

    if count_om>count_andy:
        print('Om')
    elif count_om<count_andy:
        print('Andy')
    else:
        print('Draw')

