from collections import Counter

n = int(input())

running = True

while running:
    fCount = 0

    n+=1

    New = str(n)

    List = Counter(New)

    for i,j in List.items():
        if j == 1:
            fCount += 1


    if fCount == 3 or fCount == 4:
        print(New)
        running = False
        break




