for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))

    sSum = sum(s)
    s.sort()
    print(sSum, end=" ")
    for i in range(n-1):
        sSum = sSum - s[i]
        print(sSum , end=' ')
    print('\n')
