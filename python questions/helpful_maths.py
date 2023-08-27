s = input()

newString = [ ]
outputString = ''

for i in range(len(s)):
    if i%2 == 0:
        newString.append(int(s[i]))

newString.sort(reverse=False)

for i in range(len(newString)):
    outputString += str(newString[i])
    outputString += "+"

print(outputString[0:len(outputString) - 1])
