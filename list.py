users = ['Dave', 'John', 'Sarah']
data = ['Dave', 42, True]

emptylist = []

# print('Dave' in emptylist)
# print(users[0])
# print(users[-2])
# print(users.index('Sarah'))
# print(users[0:2])
# print(users[1:])

# print(len(data))

# users.append('Elsa')

# users += ['Jason']

# users.extend(['Robert', 'Jimmy'])

# users.extend(data)

users.insert(0, 'Bob')

users[2:2] = ['Eddie', 'Alex']

del users[0]

data.clear()

users[1:1] = ['dave']
# users.sort()
users.sort(key=str.lower)
# print(users)

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
