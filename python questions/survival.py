for i in range(int(input())):
    n,x,d = map(int, input().split())

    no_of_buns = x * 5
    remain_days = n // no_of_buns

    print(remain_days + d)
