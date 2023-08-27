n = int(input())

result = input()

A,D = 0,0

for i in result:
    if i == 'A':
        A += 1
    else:
        D += 1

if A > D :
    print('Anton')
elif A == D:
    print('Friendship')
else:
    print('Danik')


