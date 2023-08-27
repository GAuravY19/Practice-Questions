t = int(input())
for i in range(t):
    n,b = map(int, input().split())
    screen = []
    for j in range(n):
        w,h,p = map(int, input().split())
        if p<=b:
            screen.append(w*h)


    if len(screen) != 0:
        print(max(screen))
    else:
        print('no tablet')
