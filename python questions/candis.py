t = int(input())
for _ in range(t):
    n = int(input())

    for k in range(2, 35):
        defn = 2**k - 1

        if n%defn != 0:
            continue

        x = n//defn
        break

    print(x)
