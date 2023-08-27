t = int(input())
for i in range(t):
    x = input()

    if x in 'Bb':
        print('BattleShip')
    elif x in 'Cc':
        print('Cruiser')
    elif x in 'Dd':
        print('Destroyer')
    elif x in 'Ff':
        print('Frigate')
