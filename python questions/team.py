count = 0
n = int(input())
for i in range(n):
    x = list(map(int, input().split()))

    if sum(x) >= 2:
        count += 1

print(count)
