t = int(input())
for i in range(t):
    n = int(input())
    s = input()

    alphabet = 'abcdefjhijklmnopqrstuvwxyz'
    s = sorted(s)

    print(alphabet.index(s[len(s)-1])+1)
