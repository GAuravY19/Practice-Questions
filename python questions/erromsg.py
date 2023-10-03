shift = input()

message = input()

first = 'qwertyuiop'
sec = 'asdfghjkl;'
third = 'zxcvbnm,./'

newmsg = ''

if shift.lower() == 'r':
    for i in range(len(message)):
        if message[i] in first:
            newmsg += first[first.index(message[i]) - 1]

        elif message[i] in sec:
            newmsg += sec[sec.index(message[i]) - 1]

        elif message[i] in third:
            newmsg += third[third.index(message[i]) - 1]

if shift.lower() == 'l':
    for i in range(len(message)):
        if message[i] in first:
            newmsg += first[first.index(message[i]) + 1]

        elif message[i] in sec:
            newmsg += sec[sec.index(message[i]) + 1]

        elif message[i] in third:
            newmsg += third[third.index(message[i]) + 1]

print(newmsg)



