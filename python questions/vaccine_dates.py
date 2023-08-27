for t in range(int(input())):
    d,l,r = map(int, input().split())

    if d>=l and d<=r:
        print("Take second dose now")
    elif d<1:
        print('Too Early')
    elif d>r:
        print('Too Late')
