import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from db_files import insert_dados
import re
import datetime
import asyncio
#import pandas as pd

dict_prefeitura = {}
urlpage = 'https://www.mogidascruzes.sp.gov.br/'
driver = webdriver.Firefox()

async def main():
    driver.get(urlpage)
    await asyncio.sleep(10)
    
    await Busca()
    #insert_dados(dict_prefeitura)
    driver.quit()
    

async def Busca():
    ids = ['data', 'vacinado', 'vacinado2', 'confirmado', 'recuperado', 'ativo', 'obito', 'enfermaria', 'uti']
    for id in ids:
        result = await find_by_id(id, driver)
        dict_prefeitura[id] = result[0].text
    
    formatar_dict(dict_prefeitura)

async def find_by_id(id, driver):
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

    asyncio.run(main())

    end_time = datetime.datetime.now()
    time = end_time - start_time
    print(f'Finalizado em {time}')

#Tempo1:semAsync: 0:00:14.305567
#Tempo2:semAsync: 0:00:00.713094
#Tempo1:comAsync: 0:00:14.699500
#Tempo2:comAsync: 0:00:00.753094