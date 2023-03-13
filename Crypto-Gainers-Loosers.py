import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import re

while True:

    url = 'https://www.coingecko.com/es/crypto-gainers-losers'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Cryptos
    cr = soup.find_all('span', class_='d-lg-inline font-normal text-3xs tw-ml-0 md:tw-ml-2 md:tw-self-center tw-text-gray-500 dark:tw-text-white dark:tw-text-opacity-60')

    nombre_Cryptos = []

    count = 0
    for i in cr:
        if count < 20:
            nombre_Cryptos.append(i.text.strip())
        else:
            break
        count += 1
        
    #Porcentaje Subida
    precio_cr = soup.find_all('span',  {'class': 'text-green', 'data-target': 'percent-change.percent'})

    precio_crypto = []
    count = 0
    for i in precio_cr:
        if count < 20:
            match = re.findall(r'\d{1,2}\.\d{1}%', i.text)
            if match:
                precio_crypto.append(match[0])
        else:
            break
        count += 1

    df = pd.DataFrame({'Crypto': nombre_Cryptos, '24 h':precio_crypto}, index=list(range(1,21)))
    print("-----------------")
    print(df)
    print("-----------------")
    
    time.sleep(60)


