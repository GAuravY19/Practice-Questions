t = int(input())
for i in range(t):
    n,k = map(int,input().split())

    a = list(map(int,input().split()))

    store = 0
    count = 1

    for i in range(n):

        if store + a[i] >= k:
            if store != 0:
                store = (store + a[i]) - k
            else:
                store = a[i] - k

        else:
            print("No", (i+1))
            break

    else:
        print('Yes')
