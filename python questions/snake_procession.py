t = int(input())
for i in range(t):
    l = int(input())
    x = input()

    count = 0
    x = x.replace(".","")
    a = len(x)

    if a%2 == 0:
        for i in range(a):
            if (i%2 == 0 and x[i] == "H"):
                count += 1

            elif (i%2 == 0 and x[i] == "H"):
                count += 1

    if a == count :
        print('Valid')
    else:
        print('Invalid')
