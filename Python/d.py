sac = {}

sac = {1: 'Apple',2:'ball'}

sac = {'name':'chad',1:[2,6,9]}

sac = {'name':'jack','age':26}

print(sac['name'])
print(sac.get('age'))
sac['age'] = 27
print(sac)

sac['adress'] = 'Domain'
print(sac)

sac.pop('age')
print(sac)

print("Adress:", sac.get('adress'))

sac.clear
print(sac)