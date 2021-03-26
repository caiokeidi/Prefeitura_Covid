import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from db_files import insert_dados
import re
import datetime
from selenium.webdriver.chrome.options import Options

dict_prefeitura = {}
urlpage = 'https://www.mogidascruzes.sp.gov.br/'

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-features=NetworkService")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="D:\Caiokeidi\Programming\chromedriver_win32/chromedriver.exe")

def main():
    driver.get(urlpage)
    time.sleep(10)
    
    Busca()
    #insert_dados(dict_prefeitura)
    print(dict_prefeitura)
    driver.quit()
    

def Busca():
    ids = ['data', 'vacinado', 'vacinado2', 'confirmado', 'recuperado', 'ativo', 'obito', 'enfermaria', 'uti']
    for id in ids:
        result = find_by_id(id, driver)
        dict_prefeitura[id] = result[0].text
    
    formatar_dict(dict_prefeitura)

def find_by_id(id, driver):
    results =  driver.find_elements_by_id(id) 
    return results
    

def formatar_dict(dict):
    for key, value in dict.items():
        if key == 'data':
            stringData = value
            dateBr = re.findall("([0-9]{2}\/[0-9]{2}\/[0-9]{4})", stringData)
            dateBr = dateBr[0]

            dia = dateBr[0:2]
            mes = dateBr[3:5]
            ano = dateBr[6:10]

            data = str(f'{ano}-{mes}-{dia}')
            dict[key] = data

        elif key in ['uti', 'enfermaria']:
            dict[key] = float(value.replace('%', '').replace(',', '.'))

        else:
            dict[key] = int(value)



if __name__ == "__main__":
    start_time = datetime.datetime.now()

    main()

    end_time = datetime.datetime.now()
    time = end_time - start_time
    print(f'Finalizado em {time}')

#Tempo1:semAsync: 0:00:14.305567
#Tempo2:semAsync: 0:00:00.713094
#Tempo1:comAsync: 0:00:14.699500
#Tempo2:comAsync: 0:00:00.753094