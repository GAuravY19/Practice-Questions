k,n,w = map(int,input().split()) ## K = price of first banana, n = dollars with soldier, w = number of banana

money = 0

for i in range(1,w):
    money += i * k

print(money)

print(abs(money - n))

