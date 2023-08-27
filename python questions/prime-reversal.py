for t in range(int(input())):
    n = int(input())
    a = input()
    b = input()

    a_1_count = a.count("1")
    a_0_count = a.count("0")

    b_1_count = b.count('1')
    b_0_count = b.count("0")

    if (a_1_count == b_1_count) and (a_0_count == b_0_count):
        print('YES')
    else:
        print('NO')
