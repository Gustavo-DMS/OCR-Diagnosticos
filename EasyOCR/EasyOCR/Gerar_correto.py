import os
import webbrowser

esperado = []
directory_RGB =r'./Fotos-RGB'
browser = webbrowser.Chrome(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
for filename in os.listdir(directory_RGB):
    # try block to handle the exception
    browser.open(fr'D:\Desktop\IC\EasyOCR\{directory_RGB}\{filename}', new=0,autoraise=False)
    try:
        my_list = []
        
        while True:
            numeros = input(f'digite o texto na img {filename}: ')
            if numeros == '//':
                my_list.clear()
                print('aqui')

            else:
                my_list.append(float(numeros))
            
    # if the input is not-integer, just print the list
    except:
        if input == '//':
            my_list.clear
        esperado.append(my_list)

print(esperado)