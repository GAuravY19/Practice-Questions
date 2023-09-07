n = int(input())

a = list(map(int,input().split()))

for i in a:
    if i == 0:
        continue
    else:
        print('HARD')
        break
else:
    print('EASY')
