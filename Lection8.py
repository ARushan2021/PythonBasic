import os

with open('123.txt', 'w') as f:
    str_list = ['Необходимо считать любой текстовый файл на вашем ПК (можно создать новый) '
                'и создать на его основе новый файл, '
                'где содержимое будет записано в обратном порядке.\n '
                'В конце программы вывести на экран оба файла - старый в '
                'неизменном виде и новый в обратном порядке.']
    f.writelines(str_list)

with open('123.txt', 'r') as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())

with open('123.txt', 'r') as f:
    str_list1 = f.readlines()
    print(str_list1)

swd = os.getcwd()
print(swd)