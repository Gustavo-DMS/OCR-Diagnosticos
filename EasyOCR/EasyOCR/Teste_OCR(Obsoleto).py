import easyocr
import os

result_BW = []
result_RGB = []
directory_BW =r'./Fotos-BW'
directory_RGB =r'./Fotos-RGB'
reader = easyocr.Reader(['en'])
for filename in os.listdir(directory_BW):
    print(filename)
    result_BW.append(reader.readtext(fr'.\{directory_BW}\{filename}',detail = 0,rotation_info = [90,180,270]))
    result_RGB.append(reader.readtext(fr'.\{directory_RGB}\{filename}',detail = 0,rotation_info = [90,180,270]))
print('resultado BW = ',result_BW)
print('resultado RGB = ',result_RGB)    
print('----------------------------------------------------------------')
