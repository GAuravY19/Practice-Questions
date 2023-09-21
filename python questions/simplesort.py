t = int(input())

for _ in range(t):
    s = list(input())

    if (s.index('a') == 2) or (s.index('c') == 0): # a --> c ke jagah pe and c --> a ke jagah pe
        s[0] = 'a'
        s[2] = 'c'
        s = ''.join(s)
        if s == 'abc':
            print('YES')
        else:
            print('NO')

    elif (s.index('a') == 1) or (s.index('b') == 0): # a --> b ke jagah pe and b --> a ke jagah pe
        s[1] = 'b'
        s[0] = 'a'
        s = ''.join(s)
        if s == 'abc':
            print('YES')
        else:
            print('NO')

    elif (s.index('b') == 2) or (s.index('c') == 1): # a --> b ke jagah pe and b --> a ke jagah pe
        s[1] = 'b'
        s[2] = 'c'
        s = ''.join(s)
        if s == 'abc':
            print('YES')
        else:
            print('NO')

    else:
        s = ''.join(s)
        if s == 'abc':
            print('YES')
        else:
            print('NO')
