t = int(input())
for i in range(t):
    s = input()

    if len(s) % 2 == 0:
        n = len(s)//2
        if s[:n] == s[n:]:
            print('YES')

        else:
            print('NO')
    else:
        print('NO')

