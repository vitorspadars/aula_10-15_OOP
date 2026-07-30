from interface.classes.csv_class import CsvProcessor


arquivo_base = './exemplo.csv'
filtro = 'estado'
limite = 'SP'

arquivo_csv = CsvProcessor(arquivo_base)
arquivo_csv.carregar_csv()
print(arquivo_csv.filtrar_por(['estado', 'preço'], ['SP', '10,50']))