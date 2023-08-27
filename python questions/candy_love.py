for t in range(int(input())):
    n = int(input())
    a = map(int,input().split())

    if sum(a) %2 !=0:
        print('YES')
    else:
        print('NO')
