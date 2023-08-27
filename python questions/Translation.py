# translation hona hai barland se birland language

word = input()
translated = input()

my_word = ''

for i in range(len(word)-1,-1,-1):
    my_word += word[i]

if my_word == translated:
    print('YES')
else:
    print('NO')
