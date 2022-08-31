with open('123.txt', 'r') as f123:
    str_list = f123.read()

str_list_rev = "".join(list(reversed(str_list)))

with open('321.txt', 'w') as f321:
    f321.writelines(str_list_rev)

with open('123.txt', 'r') as f123:
    print(f123.read())

with open('321.txt', 'r') as f321:
    print(f321.read())
