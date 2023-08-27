n = int(input())
count = 0
for i in range(n):
    x = input()

    if x == '++X' or x == "X++":
        count += 1

    elif x == "--X" or x == "X--":
        count -= 1

print(count)
