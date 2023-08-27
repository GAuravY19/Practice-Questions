n = int(input())

divisiors = [4,7,47,74,77,44,444,477,447,777,774,744]


for i in range(len(divisiors)):
    if n%divisiors[i] == 0:
        print('YES')
        break
    else:
        pass
else:
    print('NO')
