n = int(input())
s = list(map(int, input().split()))

l = s.copy()

meList = []
BroList = []

for i in range(n):
    meList.append(s[i])
    l.remove(s[i])

    if sum(meList) > sum(l):
        print(len(meList))
        break

