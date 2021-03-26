import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from db_files import insert_dados
import re
import datetime
#import pandas as pd

urlpage = 'https://www.mogidascruzes.sp.gov.br/'
driver = webdriver.Firefox()
dict_prefeitura = {}


def Busca():
    ids = ['data', 'vacinado', 'vacinado2', 'confirmado', 'recuperado', 'ativo', 'obito', 'enfermaria', 'uti']
    for id in ids:
        results = driver.find_elements_by_id(id)
        if id == 'data':
            pass    
        dict_prefeitura[id] = results[0].text
    
    formatar_dict(dict_prefeitura)
    print(dict_prefeitura)

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


driver.get(urlpage)
time.sleep(10)

Busca()
insert_dados(dict_prefeitura)

driver.quit()

