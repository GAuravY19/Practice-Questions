n = int(input())

s = input()
count = ''

zer = s.count('0')
one = s.count('1')

print(n - (2*(min(zer, one))))



