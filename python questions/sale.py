n,m = map(int,input().split())
a = list(map(int, input().split()))
sums = 0
a.sort()
for i in range(m):
         if a[i] < 0:
             sums += a[i]

print(abs(sums))

