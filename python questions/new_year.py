for _ in range(int(input())):
    n = int(input())

    rem = n/2020
    if (rem < 1):
        print('NO')
    else:
        lastdigit = n%2020
        if (lastdigit > rem):
            print("NO")
        else:
            print('YES')

