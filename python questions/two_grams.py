from collections import Counter

n = int(input())
s = input()

newlist = []

for i in range(len(s)):
    for j in range(len(s)):
        newlist.append((s[i] + s[j]))
print(newlist)

d = Counter(newlist)
print(d)
