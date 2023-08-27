t = int(input())
for i in range(t):
    n = int(input())
    x = []

    for j in range(n):
        x.append(int(input()))

    for j in x:
        if x.count(j) %2 != 0:
            print(j)
            break
