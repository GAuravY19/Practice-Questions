from collections import Counter

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    timing = Counter(a + b)

    print(max(timing.values()))
