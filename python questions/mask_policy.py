for t in range(int(input())):
    n,k = map(int, input().split())

    print(min(k, n-k))
