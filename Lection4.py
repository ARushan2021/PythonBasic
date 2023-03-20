dct = {}
dct['key'] = 'val'
print(dct)

dct2 = dict(kk1='val', kk2='val2')
print(dct2)

dct3 = dict(zip(('k1','k2'),('v1','v2')))
print(dct3)

print('kk1' in dct2)

dct4 = dct.copy() #при изменении копии, изменения вносятся и в оригинал
print(dct4)

print({}.fromkeys(['k1', 'k2', 'k3'], 111))

print(dct.get('key')) # обращение к словарю через ключ

print(dct3.items())

for k, v in dct3.items():
    print (v)

print(dct3.pop('k1'))

print(dct2.values())

for k in dct3:
    print (dct3.values())

 