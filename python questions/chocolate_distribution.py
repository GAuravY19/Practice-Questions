import math

t = int(input())

for _ in range(t):
    n = int(input())

    div = 3

    first = math.ceil(t / 3)
    t -= first
    sec = math.ceil(t // 2)
    t -= sec
    print(first, sec, t)

