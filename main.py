# import csv

# devs_rec = []

with open("meet-2.csv", encoding='utf-8-sig') as csvfile:
    file = csvfile.readlines()[4:]
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

# try:
#     a = 2/0
# except Exception as e:
#     print(e.__doc__)

my_dict = {"name": "Sidnei"}

# key = input('chave: ')
# valor1 = int(input('valor1: '))
# valor2 = input('valor2: ')


# my_dict['idade']

# try:
#     my_dict[key]
#     total = valor1 + valor2
#     print(total)
# except Exception as e:
#     print(e.__doc__)
# except KeyError:
#     print('chave incorreta')
# except TypeError:
#     total = valor1 + int(valor2)
#     print(total)


