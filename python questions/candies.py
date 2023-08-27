t = int(input())
for i in range(t):
    l = int(input())

    x = list(map(int, input().split()))

    count = False

    for i in x:
        if x.count(i) > 2:
            count = True


    if count:
        print('No')
    else:
        print('Yes')
