for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    prod = 1

    minimumValue = min(a)
    minimumIndex = a.index(minimumValue)
    minimumValue = (minimumValue + 1)
    a[minimumIndex] = minimumValue

    for i in a:
        prod *= i

    print(prod)
