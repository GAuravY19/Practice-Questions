t = int(input())
for i in range(t):
    n = int(input())
    s = input()

    c=''

    if len(s)%2 == 0:
        for j in range(0,n-1,2):
            c += (s[j+1] + s[j])
    else:
        for j in range(0,n-1,2):
            c += (s[j+1] + s[j])
        c += s[-1]

    m = ''

    lst = 'abcdefghijklmnopqrstuvwxyz'
    for j in range(n):
        m += lst[(25 - lst.index(c[j]))]

    print(m)
