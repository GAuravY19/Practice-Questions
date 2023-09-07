n = int(input())

count = 0
i = 0
while (i<n):
    s = list(map(int, input().split()))

    for j in range(len(s)-1):
        if (s[j+1] - s[j]) >= 2 :
            count += 1

    i += 1

print(count)



