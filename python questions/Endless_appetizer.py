import math

for i in range(int(input())):
    x,y,r = map(int, input().split())

    a = r//30
    z = x+y
    print(math.ceil(z/y))
