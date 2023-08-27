x = int(input())
y = int(input())

a = x*y
p = 2*(x+y)

if a>p:
    print('area',a)
elif a == p:
    print('eq')
else:
    print('peri',p)


