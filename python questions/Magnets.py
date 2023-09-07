n = int(input())
s=''
i = 0

finalGroup = 1

while (i<n):
    s += input()
    i += 1

for j in range(len(s)-1):
    if (s[j] == '1' and s[j + 1] == '1') or (s[j] == '0' and s[j + 1] == '0'):
        finalGroup += 1
    else:
        continue

print(finalGroup)
