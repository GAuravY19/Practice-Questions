n = int(input())

store = []
passengers = 0

for i in range(n):
    a,b = map(int, input().split())
    passengers = (passengers - a) + b
    store.append(passengers)

print(max(store))
