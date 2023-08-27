N,T = map(int, input().split())
a = list(map(int, input().split()))

count = 0

for i in range(N):
    if a[i] > T:
        count += 2
    else:
        count += 1

print(count)

