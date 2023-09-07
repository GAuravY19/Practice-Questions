for _ in range(int(input())):
    n,k,l = map(int, input().split()) # n --> pastries, k --> no. of people in queue, l --> my initial position
    a = list(map(int, input().split()))
    me = []
    j = 1
    for i in range(n):
        if j > k:
            j = 1

        if j == l :
            me.append(max(a))
            a.remove(max(a))
        else:
            a.remove(max(a))

        j += 1

    print(sum(me))
