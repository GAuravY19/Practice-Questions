def getCount(larger, smaller, cup, count):
    while (larger > smaller):
        larger -= cup
        smaller += cup
        count += 1

    return count

n = int(input())

for i in range(n):
    a,b,c = map(float, input().split())
    count = 0

    if a>b:
        count = getCount(larger = a, smaller = b, cup = c, count = count)
        print(count)
    else:
        count = getCount(larger = b, smaller = a, cup = c, count = count)
        print(count)


