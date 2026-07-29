import pandas as pd

def carregar_csv_e_filtrar(arquivo_csv, estado):
    # Carregar o arquivo em um DataFrame
    df = pd.read_csv(arquivo_csv)

    # Verificar e Remover células vazias
    df = df.dropna()

    # Filtrar as linhas pela coluna de estado
    df_filtrado = df[df['estado'] == estado]

    return df_filtrado


arquivo_csv = './exemplo.csv'
estado_filtrado = 'RJ'
df_filtrado = carregar_csv_e_filtrar(arquivo_csv,estado_filtrado)

print(df_filtrado)