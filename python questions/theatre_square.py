import math

n,m,a = map(int, input().split())

len = n//a
bre = m//a

if n%a != 0:
    len += 1

if m%a != 0:
    bre += 1

print(len * bre)


