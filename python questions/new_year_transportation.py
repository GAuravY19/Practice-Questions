n,t = map(int, input().split())
a = list(map(int, input().split()))

nxt = 0
pos = 1

while (pos < t):
    nxt = pos + a[pos - 1]
    pos = nxt

if pos == t:
    print('YES')
else:
    print('NO')
