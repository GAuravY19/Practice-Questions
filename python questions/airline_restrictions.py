t = int(input())
for i in range(t):
    a,b,c,d,e = map(int, input().split())

    if ((a+b) <= d) and (c <= e):
        print('Yes')
    elif ((a+c) <= d) and (b <= e):
        print('Yes')
    elif ((c+b) <= d) and (a <= e):
        print('Yes')
    else:
        print('No')
