t = int(input())
for i in range(t):
    a,b = map(int, input().split())

    x = a/(b**2)

    if x<=18:
        print('Underweight')
    elif x>=19 and x<=24:
        print('Normal weight')
    elif x>=25 and x<=29:
        print('Overweight')
    elif x>=30:
        print('Obesity')
