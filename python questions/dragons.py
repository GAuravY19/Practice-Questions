s,n = map(int, input().split())
a = []
count = False
for i in range(n):
    a.append((map(int, input().split())))

    # if s >= x :
    #     s += y
    #     count = True
    # else:
    #     count = False

if count:
    print('YES')
else:
    print('NO')

