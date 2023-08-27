t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    n = n-1
    count = 0
    while n>0:
        a.remove(a[n])
        count += 1
        n-=1

    print(count)


