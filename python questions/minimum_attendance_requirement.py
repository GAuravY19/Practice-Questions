for t in range(int(input())):
    n = int(input())
    b = input()

    b_1_count = b.count("1")

    percent = (((120 - n) + b_1_count) / 120) * 100

    if percent >= 75:
        print('YES')
    else:
        print('NO')
