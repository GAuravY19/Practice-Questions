for t in range(int(input())):
    n = int(input())
    s = input()

    c0 = s.count('0')
    c1 = s.count('1')

    if c0 >= c1:
        print(n - c0)
    else:
        print(n - c1 + 1)
