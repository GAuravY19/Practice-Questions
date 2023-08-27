while True:
    t = int(input())
    if t == 0:
        break

    x = list(map(int, input().split()))

    lst = [0]*len(x)

    for i in range(len(x)):
        k = i+1
        lst[x[i] - 1] = k

    if lst == x:
        print('ambigous')
    else:
        print('non-ambiguous')
