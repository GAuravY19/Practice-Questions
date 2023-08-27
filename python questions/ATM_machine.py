t = int(input())
for i in range(t):
    n,k = map(int, input().split())

    a = list(map(int,input().split()))
    lst = ' '

    for j in a:
        if j<=k:
            lst+= "1"
            k = k-j

        else:
            lst+="0"

    print(lst)
