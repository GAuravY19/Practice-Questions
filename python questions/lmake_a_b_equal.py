t = int(input())
for i in range(t):
    x,y = map(int, input().split())

    min_value = min(x,y)
    max_value = max(x,y)

    if min_value == max_value:
        print('yes')
    else:

        while(min_value < max_value):
            min_value = min_value *2

        if min_value == max_value:
            print('yes')
        else :
            print('no')
