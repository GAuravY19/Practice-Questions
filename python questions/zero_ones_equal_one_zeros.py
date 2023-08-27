t = int(input())
for i in range(t):
    n = int(input())

    count = ''

    for i in range(n):
        if i%2 == 0:
            count += '1'
        else:
            count += '0'

    print(count)
