t = int(input())
for i in range(t):
    a,b,m = map(int, input().split())

    A = abs(a-b)
    B = m - A

    print(min(A,B))
