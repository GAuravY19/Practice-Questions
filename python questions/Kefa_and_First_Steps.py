n = int(input())
a = list(map(int, input().split()))

count = 1
max_count = []
if n > 1:
    for i in range(n-1):
        if a[i] <= a[i + 1]:
            count += 1
            max_count.append(count)
        else:
            max_count.append(count)
            count = 1

    print(max(max_count))

else:
    print(1)


