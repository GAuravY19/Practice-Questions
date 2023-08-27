t = int(input())
for i in range(t):
    x,y,a,b = map(int, input().split())

    print((a//x) + (b//y))
