n = int(input())

if n%2 == 0:
    for i in range(1,n):
        if i%2 != 0 :
            print('I hate that', end=" ")
        else:
            print('I love that', end=" ")
    print('I love it')
else:
    for i in range(1,n):
        if (i%2) != 0 :
            print('I hate that', end=" ")
        else:
            print('I love that', end=" ")
    print('I hate it')
