import math

for _ in range(int(input())):
    l,v1,v2 = map(int, input().split())

    tor = math.ceil(l/v1)
    har = math.ceil(l/v2)

    if har < tor:
        print(tor - har  - 1)
    elif har == tor:
        print(-1)
    else:
        print(0)
