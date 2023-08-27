t = int(input())
for i in range(t):
    a,b = map(int, input().split())
    x = list(map(int, input().split()))

    if a*b - sum(x) > 0:
        print(a*b - sum(x))
    else:
        print(0)
