s = input()

letter = 'abcdefghijklmnopqrstuvwxyz'

initial = 'a'
final = 0

for i in range(len(s)):
    e = ord(s[i]) - ord(initial)

    if e < 0:
        e *= (-1)

    d = 26-e

    g = min(d,e)

    final += g

    initial = s[i]

print(final)
