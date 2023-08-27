t = int(input())
for i in range(t):
    n = int(input())
    b = list(map(int, input().split()))

    print('yes') if sum(b)%2 == 0 else print('no')
