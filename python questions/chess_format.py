t = int(input())
for i in range(t):
    a,b = map(int, input().split())

    x = a+b

    if x<3:
        print('Bullet')
    elif x>=3 and x<=10:
        print('blitz')
    elif x>=11 and x<=60:
        print('rapid')
    elif x>60:
        print('classical')
