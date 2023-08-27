def match(newString):
    pattern = '><'

    return newString.count(pattern)


for t in range(int(input())):
    s = input()

    newString = 0

    for i in range(len(s)):
        if s[i] == '>':
            newString += '<'
        elif s[i] == '<':
            newString += '>'
        else:
            newString += "*"

    count = match(newString)

    print(count)
