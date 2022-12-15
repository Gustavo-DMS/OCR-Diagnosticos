from msilib.schema import Directory
import os
import random



Directory = (r'.\Training_data')
listaNums = []
numero = 1
for files in os.listdir(Directory):
    num = files.split('.')
    formato = num[1]
    num = num[0]
    num = num.split(' ')
    num = num[1]
    num = num[1:-1]
    if num not in listaNums:
        listaNums.append(num)
    else:
        listaNums.append(numero)
    os.rename(fr'./Training_data/{files}',rf'./Training_data/{numero}.{formato}')
    numero += 1

        