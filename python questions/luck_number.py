# problem statement
'''
Petya loves lucky numbers. We all know that lucky numbers are the
positive integers whose decimal representations contain only the lucky
digits 4 and 7. For example, numbers 47, 744, 4 are lucky and 5, 17, 467
are not.

Unfortunately, not all numbers are lucky. Petya calls a number nearly
lucky if the number of lucky digits in it is a lucky number.
He wonders whether number n is a nearly lucky number.
'''

n = input()

no_lucky = 0

for i in n:
    if i == '4' or i == '7':
        no_lucky += 1

if no_lucky >= 2 and ((no_lucky == 4) or (no_lucky == 7)):
    print('YES')
else:
    print('NO')


# 4744000695826
