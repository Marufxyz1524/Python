numbers = [23,45,56,34,67,12,78,34,90,45,22]
odds = []

for num in numbers:
    if num % 2 == 1:
        odds.append(num)

print(odds)

odds_num = [num for num in numbers if num % 2 == 1 if num % 5 ==0]
print(odds_num)

players = ['sakib', 'mushfik','mustafiz']
ages = [38,54,78]

for player in players:
    print('player',player)

for age in ages:
        print(player,age)