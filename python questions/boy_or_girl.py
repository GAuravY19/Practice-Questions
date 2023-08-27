s = input()

distinct = []

for i in s:
    if i not in distinct:
        distinct.append(i)

if len(distinct) %2 == 0:
    # female
    print('CHAT WITH HER!')
else:
    print("IGNORE HIM!")
