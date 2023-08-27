first = 0
sec = 1

print(first)
print(sec)
for i in range(8):
    next = first + sec
    first, sec = sec,next
    print(next)
