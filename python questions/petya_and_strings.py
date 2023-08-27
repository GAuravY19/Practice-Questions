a = input()
b = input()

countA, countB = 0,0

order = 'abcdefghijklmnopqrstuvwxyz'

for i in range(len(a)):
    if order.index(a.lower()[i]) > order.index(b.lower()[i]):
        countA += 1
        break

    elif order.index(a.lower()[i]) < order.index(b.lower()[i]):
        countB += 1
        break

if countB > countA:
    print('-1')
elif countA > countB:
    print('1')
else:
    print('0')
