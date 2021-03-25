import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
#import pandas as pd

urlpage = 'https://www.mogidascruzes.sp.gov.br/'
driver = webdriver.Firefox()
dict_prefeitura = {}

driver.get(urlpage)
time.sleep(10)


def Busca():
    ids = ['data', 'vacinado', 'vacinado2', 'confirmado', 'recuperado', 'ativo', 'obito', 'enfermaria', 'uti']
    for id in ids:
        results = driver.find_elements_by_id(id)
        if id == 'data':
            pass

        dict_prefeitura[id] = results[0].text


Busca()
print(dict_prefeitura)
driver.quit()