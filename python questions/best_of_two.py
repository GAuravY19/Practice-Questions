t = int(input())
for i in range(t):
    a1,a2,a3,b1,b2,b3 = map(int, input().split())

    alice = (a1+a2+a3) - min(a1,a2,a3)
    bob = (b1+b2+b3) - min(b1,b2,b3)

    if alice>bob:
        print('alice')
    elif alice == bob:
        print('tie')
    else:
        print('bob')


