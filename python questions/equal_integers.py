t = int(input())
for i in range(t):
    x,y = map(int, input().split())

    if x == y:
        print(0)

    elif y>x:
        print(y-x)

    elif x>y:
        diff = x - y

        if diff %2 == 0:
            print(diff//2)
        else:
            print(diff//2 + 2)
