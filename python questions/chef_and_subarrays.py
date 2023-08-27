t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    count = 0

    for j in range(n):
        p = 1
        s = 0
        for k in range(j,n):
            p *= a[k]
            s += a[k]

            if p == s:
                count += 1

    print(count)
