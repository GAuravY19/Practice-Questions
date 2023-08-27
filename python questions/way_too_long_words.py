t = int(input())
for i in range(t):
    x = input()

    if len(x) > 10:
        a = x[:1]
        b = x[-1]
        y = str(len(x)-2)

        print(a + y + b)
    else:
        print(x)
