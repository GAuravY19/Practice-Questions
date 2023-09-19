n = int(input())

s = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
count = 0

if len(s) >= 26:
    for i in range(len(alphabet)):
        if alphabet[i] in s.lower():
            count += 1

    if count >= 26:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
