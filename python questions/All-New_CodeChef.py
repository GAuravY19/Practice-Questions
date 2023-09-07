x,y = map(int, input().split())

if x < y:
    print('Old')
elif x == y:
    print('Same')
else:
    print('New')
