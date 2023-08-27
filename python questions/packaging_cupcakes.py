t = int(input())
for i in range(t):
    n = int(input())

    if n%2 == 0:
        print(n)
    else:
        print(n - (n//2))
