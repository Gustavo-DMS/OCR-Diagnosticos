import os


directory =r'./Fotos-post'
i = 0
for filename in os.listdir(directory):
    extensao = filename.split('.')[-1]
    print(extensao)
    os.rename(fr'{directory}\{filename}',fr'.\{directory}\{i}.{extensao}')
    i +=1 
