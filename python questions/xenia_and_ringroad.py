n,m = map(int, input().split())
m_list = list(map(int, input().split()))

initial = 1
time = 0

for i in range(m):
    present = m_list[i]

    if present >= initial:
        time += present - initial
    else:
        time += n - (initial - present)

    initial = present

print(time)



