for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))

    score = 0

    for i in range(len(l) - 1):
        for j in range(i+1,len(l)):
            score += (l[i]*l[j])

    print(score)
