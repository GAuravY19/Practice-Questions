a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))
e = list(map(int, input().split()))

if (sum(a)) != 0:
    x,y = 1, a.index(1)+1

elif sum(b) != b:
    x,y = 2, b.index(1)+1

elif sum(c) != c:
    x,y = 3, c.index(1)+1

elif sum(d) != d:
    x,y = 4, d.index(1)+1

else:
    x,y = 5, e.index(1)+1


r,c = (3,3)

print(abs(r-x) + abs(c-y))
