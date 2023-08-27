t = int(input())
for i in range(t):
    n = int(input())
    m = input()

    mlist = []
    count = 0

    for j in m:
        mlist.append(m.count(j))

    for j in mlist:
        if j%2 == 0:
            count += 1

    if count == len(mlist):
        print('YES')
    else:
        print('NO')
