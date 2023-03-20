dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
dict1 = {}

for k in dict:
    if dict[k] >= 3:
        dict1[k] = dict[k]

print('Старый словарь: ', dict)
print('Новый словарь: ', dict1)
