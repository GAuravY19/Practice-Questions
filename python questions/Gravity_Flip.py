n = int(input())
lst = list(map(int, input().split()))

for j in range(n):
    for i in range(n-1):
        if lst[i] > lst[i + 1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]

for i in lst:
    print(i, end=" ")
