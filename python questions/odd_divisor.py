t = int(input())
for _ in range(t):
    n = int(input())

    if n%2 != 0:
        print('YES')
    else:
        while(n>1):
            n = n//2
            if (n%2 != 0) and (n != 1):
                print('YES')
                break
        else:
            print('NO')
