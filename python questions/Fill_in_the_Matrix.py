import random

t = int(input())

for i in range(t):
    n,m = map(int, input().split())

    for j in range(n):
        for k in range(m):
            print(random.randint(0,m), end='')
        print('\n')


