#%%
from operator import index
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# %%
url ='https://www.vivareal.com.br/venda/parana/curitiba/apartamento_residencial/?pagina={}'

# %%
i = 1
ret = requests.get(url.format(i))
soup = bs(ret.text)
# %%
houses = soup.find_all(
    'article', {'class': 'property-card__container'}
)

qtd_imoveis = float(soup.find('strong', {'class': 'results-summary__count js-total-records'}).text.replace('.', ''))
# %%
houses
# %%
qtd_imoveis
house = houses[0]
# %%
df = pd.DataFrame(
    columns=[
        'descricao',
        'endereco',
        'area',
        'quartos',
        'wc',
        'vagas',
        'valor',
        'condominio',
        'wlink_house'
    ]
)
i = 0

#%%
while qtd_imoveis > df.shape[0]:
    i += 1
    print(f"Valor i: {i}\t\t qtd_imoveis:{df.shape[0]}")
    ret = requests.get(url.format(i))
    soup = bs(ret.text)    
    houses = soup.find_all(
        'article', {'class': 'property-card__container'}
    )      
    for house in houses:
        try:
            descricao = house.find('span', {'class': 'property-card__title'}).text.strip()
        except:
            descricao = None
        try:
            endereco = house.find('span', {'class': 'property-card__address'}).text.strip()
        except:
            endereco = None
        try:
            area = house.find('span', {'class': 'property-card__detail-value js-property-card-value property-card__detail-area js-property-card-detail-area'}).text.strip()
        except:
            area = None
        try:
            quartos = house.find('li', {'class': 'property-card__detail-item property-card__detail-room js-property-detail-rooms'}).span.text.strip()
        except:
            quartos = None
        try:
            wc = house.find('li', {'class': 'property-card__detail-item property-card__detail-bathroom js-property-detail-bathroom'}).span.text.strip()
        except:
            wc = None
        try:
            vagas = house.find('li', {'class': 'property-card__detail-item property-card__detail-garage js-property-detail-garages'}).span.text.strip()
        except:
            vagas = None
        try:
            valor = house.find('div', {'property-card__price js-property-card-prices js-property-card__price-small'}).find('p').text.strip()
        except:
            valor = None
        try:
            condominio = house.find('strong', {'class': 'js-condo-price'}).text.strip()
        except:
            condominio = None
        try:
            wlink_house = 'https://www.vivareal.com.br' + house.find('a', {'class': 'property-card__content-link js-card-title'})['href']
        except:
            wlink_house = None

        df.loc[df.shape[0]] = [
            descricao,
            endereco,
            area,
            quartos,
            wc,
            vagas,
            valor,
            condominio,
            wlink_house
        ]

# %%
print(descricao)
print(endereco)
print(area)
print(quartos)
print(wc)
print(vagas)
print(valor)
print(condominio)
print(wlink_house)
# %%
df.to_csv('banco_de_imoveis.csv', sep=';', index=False)
# %%
