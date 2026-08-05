from fastapi import FastAPI
from faker import Faker
import pandas as pd
import random

app = FastAPI(debug=True)
fake = Faker()


file_name = 'data/products.csv'
df = [pd.read_csv(file_name)]
df['indice'] = range(1,len(df)+1)
df.set_index('indice', inplace=True)


lojapadraoonline = 11


@app.get('/')
async def hello_world():
    return 'Hello World'


@app.get('/gerar_compra')
async def gerar_compra():
    index = random.randint(1, len(df)-1)
    tuple = df.iloc[index]
    return [{
        'client': fake.name(),
        'creditcard': fake.credit_card_provider(),
        'product': fake.random_company_product,
        'ean': fake.ean(),
        'price': fake.currency,
        'clientPostion': fake.location_on_land(),
        'store': lojapadraoonline,
        'datetime': fake.iso8601()
    }]