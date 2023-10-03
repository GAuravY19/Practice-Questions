first = input()
sec = input()

new = ''

for i in range(len(first)):
    if first[i] == sec[i]:
        new += '0'

    else:
        new += '1'

print(new)
