import pandas as pd

#def xlsx_to_csv_pd():
    #data_xls = pd.read_excel('materials.xlsx', index_col=0)
    #data_xls.to_csv('materials.csv', encoding='utf-8')
#if __name__ == '__main__':
   # xlsx_to_csv_pd()

df = pd.read_excel('material.xlsx', 'Лист1')
df.to_csv('materials.csv', sep=';')