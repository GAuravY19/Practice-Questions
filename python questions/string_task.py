n = input()
new = ''

vowel =  "aoyeui"

for i in n.lower():
    if i in vowel:
        continue
    else:
        new += ('.' + i)

print(new)
