import pandas as pd
import os
import easyocr

writer = pd.ExcelWriter('comparison.xlsx', engine='xlsxwriter')
reader = easyocr.Reader(['en'])
directory_dataSet = r'./Data-set'
dataSets = []
index = []
esperado = [[98.0, 71.0], [124.0, 83.0, 69.0], [93.0, 11.9, 68.0], [96.0, 67.0], [93.0, 11.4, 66.0], [92.0, 11.8, 65.0], [93.0, 9.8, 66.0], [93.0, 10.4, 75.0], [93.0, 10.4, 73.0], [93.0, 11.6, 67.0], [93.0, 12.6, 69.0], [93.0, 12.5, 70.0], [124.0, 83.0, 69.0], [92.0, 12.2, 72.0], [94.0, 11.9, 70.0], [95.0, 67.0], [92.0, 70.0], [125.0, 85.0, 61.0], [91.0, 12.0, 77.0], [92.0, 68.0], [93.0, 11.8, 73.0], [93.0, 12.4, 70.0], [93.0, 12.0, 69.0], [36.1], [94.0, 12.7, 73.0], [92.0, 11.9, 76.0], [154.0, 96.0, 71.0], [97.0, 79.0], [154.0, 96.0, 71.0], [36.0], [74.0, 99.0], [36.8], [36.7], [94.0, 13.3, 73.0], [124.0, 83.0, 69.0], [96.0, 76.0], [33.7], [125.0, 85.0, 61.0], [33.7], [36.1], [36.1], [124.0, 83.0, 69.0], [116.0, 84.0, 74.0], [116.0, 84.0, 74.0], [125.0, 85.0, 61.0], [127.0, 87.0, 73.0]]
i = 0
read = []
for folders in os.listdir(directory_dataSet):
    dataSets.append(folders)
print(dataSets)
for filename in os.listdir(fr'{directory_dataSet}/{dataSets[0]}'):
    index.append(filename)
colunas = dataSets.copy()
colunas.append('Esperado')
df = pd.DataFrame([],index=index, columns=colunas)
for file in index:
    atual = esperado[i]
    i += 1
    df.loc[file] = [reader.readtext(fr'.\{directory_dataSet}\{dataSets[0]}\{file}',detail = 0,rotation_info = [90,180,270])] + [reader.readtext(fr'.\{directory_dataSet}\{dataSets[1]}\{file}',detail = 0,rotation_info = [90,180,270])] + [reader.readtext(fr'.\{directory_dataSet}\{dataSets[2]}\{file}',detail = 0,rotation_info = [90,180,270])] + [atual]
    

   
df.to_excel(writer, sheet_name='Run2', index=True)
writer.close()