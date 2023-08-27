a,b = map(int, input().split())

count = 0

while True:
    if a <= b:
        a = a*3
        b = b*2
        count += 1
    else:
        break

print(count)
