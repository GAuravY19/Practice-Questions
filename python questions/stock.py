for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))

    mini = min(s)
    s.remove(mini)

    print(sum(s))
