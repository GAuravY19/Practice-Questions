guest = input()
host = input()
joke = input()

final = guest + host
final = ''.join(sorted(final))
joke = ''.join(sorted(joke))

if final == joke:
    print('YES')
else:
    print('NO')
