import random

for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    if len(a) == 1:
        print(1)
    else:
        odd = 0
        for i in a:
            if i%2 == 1:
                odd += 1
        print(odd%2 + 1)









