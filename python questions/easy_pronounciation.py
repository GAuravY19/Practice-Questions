t = int(input())
for i in range(t):
    n = int(input())
    s = input()

    count = 0

    for j in range(n):
        if s[j] not in 'aeiou':
            count +=1
            if count >=4:
                print('NO')
                break
        else:
            count = 0

    else:
        print('YES')
