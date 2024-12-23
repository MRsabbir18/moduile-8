numbers = [45, 87, 65, 43, 85, 14, 26, 61 ,70]
odds=[]
for num in numbers:
    if num % 2 == 1 and num % 5 == 0:
        odds.append(num)

print(odds)   
#odds_nums = [num for num in numbers if num % 2 == 1]
odds_nums = [num for num in numbers if num % 2 == 1 if num % 5 == 0]
print(odds_nums)

players = ['sakib', 'musfiq','liton']
ages = [38, 38, 32]

age_comb = []
for player in players:
    print('players:', players)
    for age in ages:
        print(players, age)
        age_comb.append([player, age])
print(age_comb)        
age_comb2 = [[players,age] for player in players for age in ages]
print(age_comb2)