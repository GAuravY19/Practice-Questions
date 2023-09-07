n,k = map(int,input().split())

even = []
odd = []

if k <= (n+1)//2:
    print(int(k*2)-1)
else:
    print(int(k - (n+1)//2) * 2)

